#Write a program to check whether a given number is greater than 100 using the if..else operator.
#TernaryOpEx26.py

num=float(input("Enter a Number: "))

res = "Greater than 100" if num>100 else "Not Greater than 100"

print("{} is {}".format(num,res))