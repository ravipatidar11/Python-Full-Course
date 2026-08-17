#Write a program to check whether a number is divisible by both 3 and 5 using the if..else operator.
#TernaryOpEx17.py

num=float(input("Enter a number: "))

res= "Divisible" if (num%3==0 and num%5==0) else "Not Divisible"

print("{} is {} by both 3 and 5".format(num,res))