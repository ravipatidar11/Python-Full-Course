#Write a program to check whether a number is a perfect square root of 10 using the if..else operator.
#TernaryOpEx33.py

num=int(input("Enter Number: "))

res = "Perfect Square root of 10" if num**(1/2)==10 else "Not a Perfect Square root of 10"

print(" {} = {}".format(num,res))
