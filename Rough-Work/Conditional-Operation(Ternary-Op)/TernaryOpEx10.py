#Write a program to find the absolute value of a number using the if..else operator.
#TernaryOpEx10.py

val=float(input("Enter a number: "))

res= -1*val if val<0 else val
print("Absolute value of {} is {}".format(val,res))