def percent_calculator(no_of_subjects,exam_type,exams,sub_marks):
        divisor=0
        total=0
        if exam_type[0]==exams[0] or exam_type[0]==exams[1]:
           divisor=40*no_of_subjects
        elif exam_type[0]==exams[3] or exam_type[0]==exams[4]:
           divisor=100*no_of_subjects

        for marks in sub_marks:
            total+=float(marks)
        avg=total/divisor *100
        avg=round(avg,2)
        return avg

def grade_calculator(percentage) :  
    grade=0 
    temp=percentage   
    if temp>=85  :
        grade="S"
    elif temp>=75 :
        grade="A"
    elif temp>=65 :
        grade="B"
    elif temp>=55 :
        grade="C"
    elif temp>=45 :
        grade="D"
    elif temp>=35 :
        grade="E"
    else:
        grade="F"   
    return grade
    
def cgpaCalculator(percentage):
    CGPA=float(percentage)/9.5
    CGPA=round(CGPA,2)
    return CGPA

def placement(CGPA):
    x=""
    if CGPA >= 9:
        x="Congratulations, maintain this CGPA for good placement."
    elif CGPA>=8:
        x= "Congratulations, keep up the hard work for good placement." 
    elif CGPA>=7:
        x= "Congratulations, work a little harder for a placement."
    else:
        x="Congratulations, work hard for a placement."
    return x