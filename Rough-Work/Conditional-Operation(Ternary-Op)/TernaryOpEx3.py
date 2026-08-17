#Write a program to check whether a number is even or odd using the if..else operator
#TernaryOpEx3.py

num=int(input('Enter a number: '))

res= "even" if num%2==0 else "odd"

print("{} is ={}".format(num,res))