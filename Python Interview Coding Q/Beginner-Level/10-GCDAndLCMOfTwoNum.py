# Write a Python program to find the GCD and LCM of two numbers.
#10-GCDAndLCMOfTwoNum.py

import math

a=int(input("Enter First Value:"))
b=int(input("Enter First Value:"))

gcd=math.gcd(a,b)
print("GCD=",gcd)

lcm=math.lcm(a,b)
print("LCM=",lcm)