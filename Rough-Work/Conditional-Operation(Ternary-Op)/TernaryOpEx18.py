#Write a program to determine whether a number is a single-digit number or a multi-digit number using the if..else operator.
#TernaryOpEx18.py

num=int(input("Enter a number: "))

res = "single digit" if num<=9 else "multiple digits"

print("{} is {}".format(num,res))