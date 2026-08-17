#Write a program to find the square of an even number; otherwise find its cube using the if..else operator.
#TernaryOpEx34.py

num=int(input("Enter Number: "))

res = num**2 if num%2==0 else num**3

print("{}={}".format(num,res))