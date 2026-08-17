#Write a Python program to calculate the sum of digits of a number.
#SumOfDigitOfNum.py

num=int(input("Enter Any Number:"))
num1=num
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("Sum of digit {} = {}".format(num1,sum))