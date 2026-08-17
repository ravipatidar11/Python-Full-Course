#Generate all add ODD num. within n reversed order
#WhileLoopEx8.py

n=int(input("Enter how many number u want to generate: "))

if n<=0:
    print("Invalid Number")

else:
    print("Generating Text from {} to 1".format(n))
    while (n>0):
        if n%2!=0:
            print(n)
        n=n-1