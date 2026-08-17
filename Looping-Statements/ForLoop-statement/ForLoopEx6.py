#program for generating Mul Table for Given Number
#ForLoopEx6.py

n=int(input("Enter number u want their MUl Table: "))

if n<=0:
    print("Invalid Number")

else:
    print("MUL Table of {}".format(n))
    for i in range(1,11):
        print("{} * {} = {}".format(n,i,n*i))
    else:
        print("-"*50)