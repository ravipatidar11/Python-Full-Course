#Write a program to find the maximum among two entered numbers using the if..else operator.
#TernaryOpEx23.py

a=float(input("Enter First Number: "))
b=float(input("Enter Second Number: "))

res = a if a>b else b if b>a else "Both are Same"

print("Max({},{})={}".format(a,b,res))