#Write a program to find the greater of two numbers using the if..else operator
#TernaryOpEx1.py

a=float(input('Enter First number: '))
b=float(input('Enter Second number: '))

res= a if a>b else b if b>a else "both are equal"

print("Greater num. is =" ,res)