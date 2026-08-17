#program for Generating 1 to N where N is +VE
#WhileLoopEx1.py

n = int(input('Enter how many number u want to generate: '))

if n<=0:
    print("{} is Invalid number".format(n))

else:
    print("-"*50)
    print("\t\tNumber from 1 to {}".format(n))
    print("-" * 50)
    i=1
    while (i<=n):
        print("\t\t",i)
        i=i+1
    else:
        print("-"*50)