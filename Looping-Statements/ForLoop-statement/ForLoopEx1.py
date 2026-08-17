#program for Generating 1 to N where N is +VE
#ForLoopEx1.py

n=int(input("Enter how many number u want: "))

if n<=0:
    print("Invalid input")

else:
    print("Number from 1 to {}".format(n))
    for i in range(1,n+1):
        print(i)
    else:
        print("-"*50)