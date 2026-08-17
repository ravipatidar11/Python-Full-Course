#Write a program to find the minimum among two entered numbers using the if..else operator.
#TernaryOpEx24.py

a=float(input("Enter First Number: "))
b=float(input("Enter Second Number: "))

res = a if a<b else b if b<a else "Both are Same"

print("Min({},{})={}".format(a,b,res))