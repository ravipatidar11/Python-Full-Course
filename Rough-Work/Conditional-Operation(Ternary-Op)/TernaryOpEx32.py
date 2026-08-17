#Write a program to check whether a number is a three-digit number using the if..else operator.
#TernaryOpEx32.py

num = int(input("Enter Number: "))

res = "Three-Digit" if 100 <= num <= 999 else "Not a Three-Digit"

print("Num. is ",res)