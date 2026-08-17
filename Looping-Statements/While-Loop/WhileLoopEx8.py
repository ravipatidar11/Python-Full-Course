#Generate all add ODD num. within n
#WhileLoopEx8.py

n=int(input("Enter how many number u want to generate: "))

if n<=0:
    print("Invalid Number")

else:
    print("generate text from 1 to {}".format(n))
    i=1
    while (i<=n):
        if i%2!=0:
            print(i)
        i=i+1