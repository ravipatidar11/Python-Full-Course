##Program for Generating all Even Numbers within N
#WhileLoopEx4.py

n = int(input('Enter how many Even number u want to generate within the range: '))

if n<=0:
    print("\t\tInvalid Number")

else:
    print("Even num. from 2 to {}".format(n))
    i=2
    while (i<=n):
        print("\t\t",i)
        i=i+2
    else:
        print("-"*50)