#Write a program to check whether a given number is a multiple of 10 using the if..else operator.
#TernaryOpEx25.py

num=float(input("Enter a Number: "))

res = "Multiple of 10" if num%10==0 else "Not Multiple of 10"

print("{} is {}".format(num,res))