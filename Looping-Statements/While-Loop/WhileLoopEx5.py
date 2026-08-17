#Program for Generating all Even Numbers In reverse Order within N
#WhileLoopEx4.py

n = int(input('Enter how many Even number u want to generate within the range: '))

if n<=0:
    print("\t\tInvalid Number")

else:
    print("\t\tEven Number from {} to 2".format(n))
    if n%2 != 0:
        n = n-1
    while (n>=2):
        print("\t\t",n)
        n=n-2
    else:
        print("-"*50)