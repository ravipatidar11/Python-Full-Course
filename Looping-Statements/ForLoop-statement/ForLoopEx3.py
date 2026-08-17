#Program for Generating all Even Numbers within N
#ForLoopEx3.py

n=int(input("Enter how many Even number u want: "))

if n<=0:
    print("Invalid Input")

else:
    print("Even Numbers from 2 to {}".format(n))
    for i in range(2,n+1,2):
        print(i)
    else:
        print("-"*50)