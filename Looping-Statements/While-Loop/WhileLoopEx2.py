#program for Generating N to 1 where N is +VE
#WhileLoopEx2.py

n = int(input('Enter how many number u want to generate: '))

if n<=0:
    print("\t\t{} is Invalid")

else:
    print("-"*50)
    print("\t\tNumber from {} to 1".format(n))
    print("-" * 50)
    while (n>=1):
        print("\t\t",n)
        n=n-1
    else:
        print("-" * 50)