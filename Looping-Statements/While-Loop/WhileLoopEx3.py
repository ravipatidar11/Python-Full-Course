#Program for Generating all Even Numbers within N
#WhileLoopEx3.py

n = int(input('Enter how many Even number u want to generate within the range: '))

if n<=0:
    print("\t\tInvalid Number")

else:
    i=1
    while (i<=n):
        if i%2==0:
            print("\t\t" ,i)
        i=i+1
    else:
        print("-"*50)