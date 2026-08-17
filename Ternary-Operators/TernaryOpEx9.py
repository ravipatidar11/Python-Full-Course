#Write a program to find the largest of three numbers using nested if..else operators.
#TernaryOpEx9.py

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=float(input("Enter third number: "))

max_val= a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "All Values are Equal"

print("({},{},{})={}".format (a,b,c,max_val))