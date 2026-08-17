#Write a program to determine whether a student is eligible for a scholarship based on marks using the if..else operator.
#TernaryOpEx29.py

marks=float(input("Enter Marks: "))

res = "Eligible" if marks>=75 else "Not Eligible"

print("Student is " ,res)