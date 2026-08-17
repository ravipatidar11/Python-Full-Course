#Program for Finding the Sum of N Natural Numbers
#ForLoopEx8.py

n=int(input("Enter a Natural number: "))

if n<=0:
    print("Invalid Number")

else:

    s=0 # Here 's' is called (Additive Identity) ---- used for accumulating sum of currently generated values by the Loop.

    print("Sum of Natural num. from 1 to {}".format(n))
    for i in range(1,n+1):
        s=s+i
        print(i)
    else:
        print("-"*50)
        print("sum={}".format(s))
        print("-"*50)