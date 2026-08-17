#Write a program to find the cube of a number if it is positive; otherwise print its square using the if..else operator.
#TernaryOpEx31.py

num=float(input("Enter Number: "))

res = num**3 if num>0  else num**2 

print(" {} = {}".format(num,res))
