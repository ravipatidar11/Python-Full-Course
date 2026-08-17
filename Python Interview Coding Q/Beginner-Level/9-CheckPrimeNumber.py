# Write a Python program to check whether a number is prime.
#9-CheckPrimeNumber.py

n=int(input("Enter Any number:"))
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
if prime:
    print("{} is Prime Number".format(n))
else:
    print("{} is not Prime Number".format(n))