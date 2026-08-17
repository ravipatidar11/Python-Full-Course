#Write a program to calculate the grade of a student (A, B, C, or F) using nested if..else operators.
#TernaryOpEx8.py

marks= float(input("Enter marks: "))

res= "A" if marks>=75 else "B" if marks>=60 else "C" if marks>=33 else "F"

print("Grade of Student is =" ,res)