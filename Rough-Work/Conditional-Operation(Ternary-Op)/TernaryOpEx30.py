#Write a program to compare two strings and display whether they are equal or not using the if..else operator.
#TernaryOpEx30.py

str1=input("Enter String1: ")
str2=input("Enter String2: ")

res = "Equal" if str1==str2 else "Not Equal"

print("({},{})={}".format(str1,str2,res))