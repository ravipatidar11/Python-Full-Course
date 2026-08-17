#program for generating Mul Table for Given Number
#WhileLoopEx6.py

n = int(input("Enter the num. u want to create mul. table: "))

if n<=0:
    print("Invalid Number")

else:
    print("mul table of {}".format(n))
    print("-" * 50)
    i=1
    while (i<=10):
        print("{} * {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("-"*50)