#Write a program to find the smaller of two numbers using the if..else operator.
#TernaryOpEx2.py

a=float(input('Enter First number: '))
b=float(input('Enter Second number: '))

res= a if a<b else b if b<a else "both are equal"

print("Smallest num. is =" ,res)