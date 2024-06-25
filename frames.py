from tkinter import*
import ISA1
import ISA2
import ASSIGNMENT
import studentdata
import esa
import aggregate

login_frame=[]
no_of_subjects=5
studentID=[]

def Change2MarksFrame(str,ID,exam_type,exams,student_frame,root,loginframe=None,loginentry=None):
        studentID.clear()
        studentID.extend(ID)
        exam_type.clear()
        exam_type.append(str)
        if len(login_frame)==0 and loginframe!=None:
           login_frame.append(loginframe)
        student_frame.pack_forget()
        marks_list=studentdata.find_exam(ID,exam_type)
        #if marks_list!=None and marks_list!=False:
        if marks_list!=None:
            if exam_type[0]==exams[0]:
                ISA1.isa1UI(root,exam_type,studentID,1,marks_list)
            elif exam_type[0]==exams[1]:
                ISA2.isa2UI(root,exam_type,studentID,1,marks_list)
            elif exam_type[0]==exams[2]:
                ASSIGNMENT.assignmentUI(root,exam_type,studentID,1,marks_list)
            elif exam_type[0]==exams[3]:
                esa.esaUI(root,exam_type,studentID,1,marks_list)
            else:
                aggregate.overallUI(root,exam_type,studentID,1,marks_list,percentage=marks_list[no_of_subjects+1],grade=marks_list[no_of_subjects+2]) 
        else:
            if exam_type[0]==exams[0]:
                ISA1.isa1UI(root,exam_type,studentID,0,marks_list)
            elif exam_type[0]==exams[1]:
                ISA2.isa2UI(root,exam_type,studentID,0,marks_list)
            elif exam_type[0]==exams[2]:
                ASSIGNMENT.assignmentUI(root,exam_type,studentID,0,marks_list)
            elif exam_type[0]==exams[3]:
                esa.esaUI(root,exam_type,studentID,0,marks_list)
            else:
                '''if marks_list==False:
                     x=open(f"{studentID[0]}.txt",mode="a")
                     x.close()'''     
                flag,missing_exams=studentdata.overall_examscheck(studentID,exams)
                if not flag:
                   aggregate.overallUI(root,exam_type,studentID,0,marks_list,missing_exams=missing_exams) 
                else:
                    overall_submarks,percentage,grade=studentdata.findSubMarks(studentID,no_of_subjects,exams,exam_type)
                    studentdata.saveMarks(studentID,exam_type,overall_submarks,percentage,grade)
                    exam=[f"{exam_type[0]}"]
                    overall_submarks=exam+overall_submarks
                    aggregate.overallUI(root,exam_type,studentID,1,overall_submarks,percentage=percentage,grade=grade)

def Change2LoginFrame(student_frame,loginframe=None,loginentry=None):
        if len(login_frame)==0 and loginframe!=None:
           login_frame.append(loginframe)
        student_frame.pack_forget()
        login_frame[0].pack(fill="both",expand=1,padx=10,pady=10)
        
        