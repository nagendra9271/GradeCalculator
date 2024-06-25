import os
import calculator
import properties
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "kandula@mysql",
    database = "nagendb"
)

cursor=db.cursor()

def file_exist(studentID):
    file_path = f"{properties.file()[0]}{studentID[0]}.txt"
    return os.path.exists(file_path)

def find_lines(marks_file):
    length = len(marks_file.readlines())
    marks_file.seek(0)  # Reset file pointer to the beginning
    return length

def id_check1(roll_no):
    with open("login.txt",mode="r") as login_file:
        login_file.seek(0)
        length = find_lines(login_file)
        for i in range(length):
            line = login_file.readline()  # Read a line from the file
            student_details=line.split(",")
            st_id = student_details[0]
            if st_id == roll_no:
                return True,student_details
            else:
                student_details.clear()
        return False,False

def id_check(roll_no):
    cursor.execute("select * from student where student_id= %s",(roll_no,))
    student_details=cursor.fetchone()
    student_details=list(student_details)
    if student_details !=None:
        return True,student_details
    else:
        return False,False
    
def find_exam1(studentID,exam_type):
    if file_exist(studentID) :
        with open(f"{studentID[0]}.txt", mode="r") as marks_file:
            marks_file.seek(0)
            length=find_lines(marks_file)
            for i in range(length):
                line=marks_file.readline()
                marks_list=line.split(",")
                if exam_type[0]==marks_list[0]:
                    return marks_list
        return None
    else:
        return False

def  find_exam(studentID,exam_type):
    cursor.execute("select * from  marks where student_id= %s and exam=%s",(studentID[0],exam_type[0]))
    marks=cursor.fetchone()
    if marks !=None:
        marks=list(marks)
        marks.remove(studentID[0])
    return marks 

def saveMarks1(studentID,exam_type,sub_marks,percentage=None,grade=None):
    with open(f"{studentID[0]}.txt", mode="+a") as marks_file:
        #To check Cursor is at the beginning of a new line or not 
        # Get the current position of the file cursor
        current_position = marks_file.tell()
        # Move the cursor to the previous newline character
        if current_position!=0:
            marks_file.seek(current_position - 1)
        # Read the character at the current cursor position
            char = marks_file.read(1)
        if current_position==0 or char=="\n" :
            marks_file.write(f"{exam_type[0]}")
        else:
            marks_file.write("\n"+exam_type[0])
        for i in sub_marks:
            marks_file.write(f",{i}")
        if percentage!=None:
            marks_file.write(f",{percentage}")
            marks_file.write(f",{grade}")

def saveMarks(studentID,exam_type,sub_marks,percentage=None,grade=None):
    if percentage!=None:
        cursor.execute("insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(exam_type[0],sub_marks[0],sub_marks[1],sub_marks[2],sub_marks[3],sub_marks[4],percentage,grade,studentID[0]))
   # cursor.execute("insert into marks(sub1,sub2,sub3,sub4,sub5) values()",())
    else:
        cursor.execute("insert into marks(exam,sub1,sub2,sub3,sub4,sub5,student_id) values(%s,%s,%s,%s,%s,%s,%s)",(exam_type[0],sub_marks[0],sub_marks[1],sub_marks[2],sub_marks[3],sub_marks[4],studentID[0]))
    db.commit()

def overall_examscheck1(studentID,exams):
        if not file_exist(studentID):
            return False
        exams_present = []
        with open(f"{studentID[0]}.txt", mode="r") as marks_file:
            marks_file.seek(0)
            length = find_lines(marks_file)
            for i in range(length):
                line = marks_file.readline()
                marks_list = line.split(",")
                exams_present.append(marks_list[0])
        if len(exams_present) < len(exams)-1:
            x=[exams[4]]
            exams_set = set(exams)-set(x)
            missing_exams = exams_set - set(exams_present)
            return False,missing_exams
        else:
            return True,True
def overall_examscheck(studentID,exams):
    cursor.execute("select exam from marks where student_id= %s",(studentID[0],))
    exams_present=cursor.fetchall()
    if len(exams_present)<len(exams)-1:
        #converting list of tuples into list
        exams_present_list=[]
        for exam_tuple in exams_present:
            for exam in exam_tuple:
                exams_present_list.append(exam)
        #removing overall from exams
        x=exams
        x.pop()
        exams_set = set(x)
        missing_exams = exams_set - set(exams_present_list)
        return False,missing_exams
    else:
        return True,True

def findSubMarks1(studentID,no_of_subjects,exams,exam_type):
    sub_marks=[]
    exams_order=[]
    with open(f"{studentID[0]}.txt", mode="r") as marks_file:
            marks_file.seek(0)
            length = find_lines(marks_file)
            for j in range(no_of_subjects):
                marks_file.seek(0)
                for i in range(length):
                    line = marks_file.readline()
                    marks_list = line.split(",")
                    if j==0:
                        exams_order.append(marks_list[0])
                    sub_marks.append(marks_list[j+1])
    overall_submarks,percentage,grade=calculateOverallMarks(no_of_subjects,exams_order,exams,exam_type,sub_marks)
    return overall_submarks,percentage,grade

def findSubMarks(studentID,no_of_subjects,exams,exam_type):
    sub_marks=[]
    exams_order=[]
    cursor.execute("select * from marks where student_id=%s",(studentID[0],))
    subs_marks=cursor.fetchall()
    for marksForEachExam in subs_marks:
        for x,i in zip(marksForEachExam,range(no_of_subjects+1)):
               if i==0:
                    exams_order.append(x)
               else:
                    sub_marks.append(x)
    overall_submarks=calculateOverallMarks(no_of_subjects,exams_order,exams,exam_type,sub_marks)
    return overall_submarks 
                  
def calculateOverallMarks(no_of_subjects,exams_order,exams,exam_type,sub_marks):
    overall_submarks=[]
    temp=0
    divisor=0
    for j in range(no_of_subjects):
        temp=0
        for i in range(len(exams_order)):
            if exams_order[i] == exams[0] or exams_order[i] == exams[1] or exams_order[i] == exams[3]:
                divisor=2
            elif exams_order[i]==exams[2] :
                divisor=1
            temp+=float(float(sub_marks[no_of_subjects*i+j])/divisor)
        overall_submarks.append(temp)

    percentage=calculator.percent_calculator(no_of_subjects,exam_type,exams,overall_submarks)
    grade=calculator.grade_calculator(percentage)
    return overall_submarks,percentage,grade