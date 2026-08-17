#StudentMarksReportEx.py
#Validation on student Number--100-200
while(True):
    sno=input("Enter the Student Number: ")
    if (sno.isdigit()):
        if int(sno) in range(100,201):
            break
        print("Invalid Number")
    else:
        print("Invalid Number")

#Validation on student Name
while(True):
    name=input("Enter the Student Name: ")
    if (name.isspace()):
        print("Don't enter Space")
    else:
        words=name.split()
        if len(words)==0:
            print("You Must entered the Name")
        else:
            res=True
            for word in words:
                if( not word.isalpha()):
                    res=False
                    break
            if res:
                name = " ".join(words)
                break
            else:
                print("Invalid Name --- Try Again")

#Validation on Marks in C Lang--0-100
while(True):
    cm=input("Enter the Student Marks in C Lang: ")
    if (cm.isdigit()):
        if int(cm) in range(0,101):
            break
        print("Invalid Number")
    else:
        print("Invalid Number")

#Validation on Marks in CPP Lang--0-100
while(True):
    cppm=input("Enter the Student Marks in CPP Lang: ")
    if (cppm.isdigit()):
        if int(cppm) in range(0,101):
            break
        print("Invalid Number")
    else:
        print("Invalid Number")

#Validation on Marks in PYTHON Lang--0-100
while(True):
    pym=input("Enter the Student Marks in PYTHON Lang: ")
    if (pym.isdigit()):
        if int(pym) in range(0,101):
            break
        print("Invalid Number")
    else:
        print("Invalid Number")
print("---------------------------------------------------------")

#Cal totmal marks and percentage
totMarks=int(cm)+int(cppm)+int(pym)
per=float(totMarks/300)*100

#Grade
if int(cm)<40 or int(cppm)<40 or int(pym)<40:
    Grade="Student is Fail"
else:
    if float(per)>=75.0:
        Grade="DISTINCTION"
    elif float(per)>=60.0:
        Grade="FIRST"
    elif float(per)>=50.0:
        Grade="SECOND"
    elif float(per)>=40.0:
        Grade="THIRD"
    else:
        Grade="FAIL"

print("Student Marks Report")
print("-"*50)
print("Student Number: ",sno)
print("Student Name: ",name)
print("Student Marks in C: ",cm)
print("Student Marks in CPP: ",cppm)
print("Student Marks in PYTHON: ",pym)
print("Student Total Marks: ",totMarks)
print("Student Percentage: ",per)
print("Student Grade:",Grade)
print("-"*50)

