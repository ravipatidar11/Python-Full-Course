# Write a Python program to calculate the factorial of a number.
#7-FactorialOfNumber.py

num=int(input("Enter Any number: "))

fact=1
for ch in range(num,0,-1):
    fact=fact*ch
print("Factorial of {} is {}".format(num,fact))