#Write a program to find the absolute difference between two numbers using the if..else operator.
#TernaryOpEx11.py

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

res= a-b if (a-b)>=0 else -(a-b)

print("absolute difference = ",res)