#Write a program to check whether a given year is a leap year using the if..else operator.
#TernaryOpEx12.py

year=int(input("Enter a year: "))

res= "Leap Year" if (year%400==0) or (year%4==0 and year%100!=0) else "Not Leap Year"

print("{}={}".format(year,res))