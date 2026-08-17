#Write a program to check whether a number is positive or negative using the if..else operator.
#TernaryOpEx4.py

num=int(input('Enter a number: '))

res= "+ve" if num>0 else "-ve"

print("{} is {}".format(num,res))
