# Write a Python program to swap two variables without using third variable.
#11-SwapTwoNum.py

a=int(input("Enter First Value:"))
b=int(input("Enter First Value:"))


#method-1
"""print("Before Swapping: a=",a)
print("Before Swapping: b=",b)
print("--------------------------")
a=a^b
b=a^b
a=a^b
print("After Swapping: a=",a)
print("After Swapping: b=",b)"""


#method-2
print("Before Swapping: a=",a)
print("Before Swapping: b=",b)
print("--------------------------")
a,b=b,a
print("After Swapping: a=",a)
print("After Swapping: b=",b)