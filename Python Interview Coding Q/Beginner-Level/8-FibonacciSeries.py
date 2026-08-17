# Write a Python program to generate the Fibonacci series up to N terms.
#8-FibonacciSeries.py

#0,1,1,2,3,5,8,13,21,34,.........

num=int(input("Enter upto how many Terms U Want:"))
series=[]
a,b=0,1
for i in range(num):
    series.append(a)
    a,b=b,a+b

print("Fibonacci Series upto {} = {}".format(num,series))