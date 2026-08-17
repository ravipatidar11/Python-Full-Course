#Program for Generating all Even Numbers In reverse Order within N
#ForLoopEx4.py

n=int(input("Enter how many Even number u want to Reversed: "))

if n<=0:
    print("Invalid Input")

else:
    if n%2!=0:
        n=n-1
        print("Even")
    else:
        print("Odd")
    print("Reversed Even from {} to 2".format(n))
    for i in range(n,1,-2):
        print(i)
    else:
        print("-"*50)