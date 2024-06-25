from tkinter import*
import frames
import calculator
import properties

studentID=[]
exams=["ISA1","ISA2","ASSIGNMENT","ESA","AGGREGATE"]

def Back2StudentFrame(overall_frame,root):  
    exam_status=[] 
    overall_frame.pack_forget()
    
    student_frame = LabelFrame(root, padx=50, pady=50)
    student_frame.pack(fill="both",expand=1,padx=10,pady=10)

    student_label1=Label(student_frame,font=("Arial",20),fg="orange")
    student_label1.grid(row=0, column=0,columnspan=5)

    student_label2=Label(student_frame,font=("Arial",20),fg="orange")
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

def overallUI(root,exam_type,ID,flag,marks_list,percentage=None,grade=None,missing_exams=None):
    studentID.clear()
    studentID.extend(ID)
    no_of_subjects=5
    exam_validation=[]
    overall_marks=[]
    overall_pgcp=[]
    subjects=properties.sub()

    overall_frame=LabelFrame(root,padx=50,pady=50)
    overall_frame.pack(fill="both", expand=1, padx=10, pady=10)

    overall_label=Label(overall_frame,font=("Arial",13))
    overall_label.grid(row=1,column=0,padx=10,pady=10,columnspan=2)

    overall_label=Label(overall_frame,text=f"{exams[4]} MARKS",font=("Arial",13))
    overall_label.grid(row=1,column=2,padx=40,pady=40)

    student_ID=Label(overall_frame,text=f"SRN:{studentID[0]}",font=("Arial",13),fg="blue")
    student_ID.place(x=0,y=10)

    student_name=Label(overall_frame,text=f"Name:{studentID[1]}",font=("Arial",13),fg="blue")
    student_name.place(x=600,y=10)

    for x in range(no_of_subjects) :
        overall_label_sub=Label(overall_frame,text=f"Total marks  of {subjects[x]}:",font=("Arial",13))
        overall_label_sub.grid(row=x+2,column=0,padx=10,pady=10,columnspan=2)

    for x in range(no_of_subjects) :
        overall_mark=Label(overall_frame,font=("Arial",13))
        overall_mark.grid(row=x+2,column=2,padx=10,pady=10)
        overall_marks.append(overall_mark)

    overall_examsvalid_label=Label(overall_frame,font=("Arial",15))
    overall_examsvalid_label.grid(row=no_of_subjects+2,column=0,padx=10,pady=10,columnspan=3)
    exam_validation.append(overall_examsvalid_label)

    overall_percentlabel=Label(overall_frame,text="PERCENTAGE:",font=("Arial",13))
    overall_percentlabel.grid(row=no_of_subjects+3,column=0,padx=10,pady=10,columnspan=2)

    overall_percent=Label(overall_frame,font=("Arial",13))
    overall_percent.grid(row=no_of_subjects+3,column=2,padx=10,pady=10)
    overall_pgcp.append(overall_percent)

    overall_gradelabel=Label(overall_frame,text="GRADE:",font=("Arial",13))
    overall_gradelabel.grid(row=no_of_subjects+4,column=0,padx=10,pady=10,columnspan=2)

    overall_grade=Label(overall_frame,font=("Arial",13))
    overall_grade.grid(row=no_of_subjects+4,column=2,padx=10,pady=10)
    overall_pgcp.append(overall_grade)

    overall_CGPAlabel=Label(overall_frame,text="CGPA:",font=("Arial",13))
    overall_CGPAlabel.grid(row=no_of_subjects+5,column=0,padx=10,pady=10,columnspan=2)

    overall_CGPA=Label(overall_frame,font=("Arial",13))
    overall_CGPA.grid(row=no_of_subjects+5,column=2,padx=10,pady=10)
    overall_pgcp.append(overall_CGPA)

    overall_placement_label=Label(overall_frame,text="PLACEMENT:",font=("Arial",13))
    overall_placement_label.grid(row=no_of_subjects+6,column=0,pady=10,columnspan=2)

    overall_placement=Label(overall_frame,font=("Arial",13),fg="blue")
    overall_placement.grid(row=no_of_subjects+6,column=2,pady=10,columnspan=3)
    overall_pgcp.append(overall_placement)

    overall_back2student=Button(overall_frame,text="BACK",width=10,height=2,font=("Arial",13),command=lambda:Back2StudentFrame(overall_frame,root))
    overall_back2student.grid(row=no_of_subjects+7,column=0,padx=50,pady=50)
    
    if flag==1:
        for x,overall_marks in zip(range(no_of_subjects),overall_marks):
            overall_marks.config(text=marks_list[x+1])
            overall_percent.config(text=percentage)
            overall_grade.config(text=grade)
            CGPA=calculator.cgpaCalculator(percentage)
            overall_CGPA.config(text=CGPA)
            overall_placement.config(text=f"{calculator.placement(CGPA)}")
    else:
        overall_examsvalid_label.config(text=f"{missing_exams} exams marks are not there")

    root.mainloop()