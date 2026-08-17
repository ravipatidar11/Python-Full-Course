#Write a program to check whether a number is divisible by 5 using the if..else operator
#TernaryOpEx16.py

num=float(input("Enter a number: "))

res= "divisible" if num%5==0 else "not divisible"

print("{} is {} by 5".format(num,res))