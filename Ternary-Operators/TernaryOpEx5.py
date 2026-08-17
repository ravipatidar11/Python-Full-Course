#Write a program to check whether a number is positive, negative, or zero using nested if..else operators.
#TernaryOpEx5.py

num=int(input('Enter a number: '))

res= "+ve" if num>0 else "-ve" if num<0 else "ZERO"

print("{} is {}".format(num,res))