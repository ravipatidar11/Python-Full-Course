#Write a program to determine whether a student has passed or failed based on marks using the if..else operator
#TernaryOpEx7.py

while(True):
    marks=float(input("Enter marks:"))
    if marks>100 or marks<0:
        print("Invalid Marks")
        continue
    if marks>=33:
        print("Pass")
    else:
        print("Fail")
    break