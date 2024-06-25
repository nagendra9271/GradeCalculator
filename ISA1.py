from tkinter import*
import frames
import studentdata
import calculator
import properties

studentID=[]
exams=["ISA1","ISA2","ASSIGNMENT","ESA","AGGREGATE"]

def marksValidation(no_of_subjects,exam_type,my_entries,marks_valid,marks_pgs) :
    flag=0
    lowest=0
    highest=40
    labels=[]
    sub_marks=[]
    for entries in my_entries :
        sub_marks.append(entries.get())
    for marks in sub_marks: 
        if marks.isdigit() :
            if  int(marks)<lowest or int(marks)>highest:
                labels.append(f"range {lowest} to {highest}")
                flag=1
            else:
                labels.append("")      
        else:
            labels.append("enter digits only")
            flag=1

    if flag==1:
        for x,y,marks_valid,marks_entry in zip(range(no_of_subjects), labels,marks_valid,my_entries):
            if y=="":
                marks_valid.config(text="")
            else:
                marks_entry.delete(0,END)
                marks_valid.config(text=y)
                marks_valid.grid(row=x+2,column=2,padx=10,pady=10,columnspan=2)
    else:
        for marks_valid in marks_valid:
            marks_valid.config(text="")
        marks_pgs[2].config(state="disabled")
        percentage=calculator.percent_calculator(no_of_subjects,exam_type,exams,sub_marks)
        grade=calculator.grade_calculator(percentage)
        marks_pgs[0].config(text=percentage)
        marks_pgs[1].config(text=grade)
        studentdata.saveMarks(studentID,exam_type,sub_marks,percentage,grade)


def Back2StudentFrame(marks_frame,root):  
    exam_status=[] 
    marks_frame.pack_forget()

    student_frame = LabelFrame(root, padx=50, pady=50)
    student_frame.pack(fill="both",expand=1,padx=10,pady=10)

    student_label1=Label(student_frame,font=("Arial",20),fg="orange")
    student_label1.grid(row=0, column=0,columnspan=5)

    student_label2=Label(student_frame,font=("Arial",20),fg="blue")
    student_label2.grid(row=3, column=0,columnspan=5)

    student_ID=Label(student_frame,text=f"SRN:{studentID[0]}",font=("Arial",13),fg="blue")
    student_ID.place(x=0,y=10)

    student_name=Label(student_frame,text=f"Name:{studentID[1]}",font=("Arial",13),fg="blue")
    student_name.place(x=600,y=10)

    student_label3=Label(student_frame,text="WELCOME TO STUDENT GRADING SYSTEM",font=("Arial",20),fg="green")
    student_label3.grid(row=4, column=0,columnspan=5)

    for x,y in zip(exams,range(5)):
        student_exam_button = Button(student_frame, text=x,width=11, height=2,font=("Arial",13),command=lambda exam_type=x:frames.Change2MarksFrame(exam_type,studentID,exam_status,exams,student_frame,root))
        student_exam_button.grid(row=1, column=y,padx=5,pady=20)
    
    logout_button = Button(student_frame, text="LOGOUT", command=lambda:frames.Change2LoginFrame(student_frame),width=10, height=2,font=("Arial",13))
    logout_button.grid(row=1,column=len(exams)) 
    
def isa1UI(root,exam_type,ID,flag,marks_list):
    studentID.clear()
    studentID.extend(ID)
    my_entries=[]
    marks_valids=[]
    no_of_subjects=5
    marks_pgs=[]
    subjects=properties.sub()
    
    marks_frame=LabelFrame(root,padx=50,pady=50)
    marks_frame.pack(fill="both", expand=1, padx=10, pady=10)
 
    student_ID=Label(marks_frame,text=f"SRN:{studentID[0]}",font=("Arial",13),fg="blue")
    student_ID.place(x=0,y=10)

    student_name=Label(marks_frame,text=f"Name:{studentID[1]}",font=("Arial",13),fg="blue")
    student_name.place(x=600,y=10)

    marks_exam_label=Label(marks_frame,font=("Arial",13))
    marks_exam_label.grid(row=1,column=0,padx=10,pady=10)

    marks_exam_label=Label(marks_frame,text=f"{exams[0]} MARKS",font=("Arial",13))
    marks_exam_label.grid(row=1,column=1,padx=40,pady=40)

    for x in range(no_of_subjects) :
        marks_label=Label(marks_frame,text=f"{subjects[x]}:",width=5,height=2,font=("Arial",13))
        marks_label.grid(row=x+2,column=0,padx=10,pady=10)

    for x in range(no_of_subjects) :
        marks_entry=Entry(marks_frame,borderwidth=10,font=("Arial",13))
        marks_entry.grid(row=x+2,column=1,padx=10,pady=10)
        my_entries.append(marks_entry)

    for x in range(no_of_subjects) :
        marks_valid=Label(marks_frame,font=("Arial",13))
        marks_valid.grid(row=x+2,column=2,padx=10,pady=10,columnspan=2)
        marks_valids.append(marks_valid)

    marks_percentlabel=Label(marks_frame,text="PERCENTAGE:",font=("Arial",13))
    marks_percentlabel.grid(row=no_of_subjects+3,column=0,padx=10,pady=10)

    marks_percent=Label(marks_frame,font=("Arial",13))
    marks_percent.grid(row=no_of_subjects+3,column=1,padx=10,pady=10)
    marks_pgs.append(marks_percent)

    marks_gradelabel=Label(marks_frame,text="GRADE:",font=("Arial",13))
    marks_gradelabel.grid(row=no_of_subjects+4,column=0,padx=10,pady=10)

    marks_grade=Label(marks_frame,font=("Arial",13))
    marks_grade.grid(row=no_of_subjects+4,column=1,padx=10,pady=10)
    marks_pgs.append(marks_grade)

    marks_save=Button(marks_frame,text="SAVE & CALCULATE",command=lambda:marksValidation(no_of_subjects,exam_type,my_entries,marks_valids,marks_pgs),width=20,height=2,font=("Arial",13))
    marks_save.grid(row=no_of_subjects+5,column=0,padx=50,pady=50)
    marks_pgs.append(marks_save)

    marks_back2student=Button(marks_frame,text="BACK",width=10,height=2,font=("Arial",13),command=lambda:Back2StudentFrame(marks_frame,root))
    marks_back2student.grid(row=no_of_subjects+5,column=1,padx=50,pady=50)
    if flag==1:
        marks_save.config(state="disabled")
        for x,marks_entry in zip(range(no_of_subjects),my_entries):
            marks_entry.insert(0,marks_list[x+1])
            marks_entry.config(state="readonly")
        marks_percent.config(text=marks_list[no_of_subjects+1])
        marks_grade.config(text=marks_list[no_of_subjects+2])
    
    root.mainloop()

    