from tkinter import *
import studentdata
import frames
import properties

studentID=[]
exams=["ISA1","ISA2","ASSIGNMENT","ESA","AGGREGATE"]
exam_status=[]

def rollNumberCheck(roll_no):
    flag,student_details=studentdata.id_check(roll_no)
    if not flag:
        roll_not_foundlabel.config(text="Not found",fg="red")
        login_entry.delete(0, END)
    else:
         studentID.clear()
         studentID.extend(student_details)
         login_entry.delete(0,END)
         changeToStudentFrame()
        
def changeToStudentFrame():
    login_frame.pack_forget()
    student_ID.config(text=f"SRN:{studentID[0]}")
    student_name.config(text=f"Name:{studentID[1]}")
    student_frame.pack(fill="both",expand=1,padx=10,pady=10)
    

root = Tk()
root.geometry("900x900")
root.title("PES UNIVERSITY")
root.iconbitmap(properties.logoFile()[0])

login_frame = LabelFrame(root, text="WELCOME TO SGS PORTAL", padx=100, pady=100, fg="blue")
login_frame.pack(fill="both", expand=1, padx=10, pady=10)

login_label = Label(login_frame, text="ROLL NUMBER:", padx=20, pady=50,font=("Arial",13))
login_label.grid(row=0,column=0,padx=5, pady=5)

login_entry = Entry(login_frame, width=30, borderwidth=5,font=("Arial",13))
login_entry.grid(row=0, column=1)

roll_not_foundlabel = Label(login_frame,text="",font=("Arial",13))
roll_not_foundlabel.grid(row=0, column=2)

login_button = Button(login_frame, text="LOGIN",command=lambda:rollNumberCheck(login_entry.get()),width=10, height=2,font=("Arial",13))
login_button.grid(row=2, column=1,padx=50,pady=50)

student_frame = LabelFrame(root, padx=50, pady=50)

student_label1=Label(student_frame,font=("Arial",20),fg="orange")
student_label1.grid(row=0, column=0,columnspan=5)

student_ID=Label(student_frame,font=("Arial",13),fg="blue")
student_ID.place(x=0,y=10)

student_name=Label(student_frame,font=("Arial",13),fg="blue")
student_name.place(x=600,y=10)

student_label2=Label(student_frame,font=("Arial",20),fg="orange")
student_label2.grid(row=3, column=0,columnspan=5)

student_label3=Label(student_frame,text="WELCOME TO STUDENT GRADING SYSTEM",font=("Arial",20),fg="green")
student_label3.grid(row=4, column=0,columnspan=6)

for x,y in zip(exams,range(5)):
    student_exam_button = Button(student_frame, text=x,width=11, height=2,font=("Arial",13),command=lambda exam_type=x:frames.Change2MarksFrame(exam_type,studentID,exam_status,exams,student_frame,root,login_frame,login_entry))
    student_exam_button.grid(row=1, column=y,padx=5,pady=20)

logout_button = Button(student_frame, text="LOGOUT", command=lambda:frames.Change2LoginFrame(student_frame,login_frame,login_entry),width=10, height=2,font=("Arial",13))
logout_button.grid(row=1,column=len(exams))

root.mainloop()