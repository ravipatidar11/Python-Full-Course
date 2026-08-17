#Program for Generating all Odd Numbers In reverse Order within N
#ForLoopEx5.py

n=int(input("Enter how many Odd number u want to Reversed: "))

if n<=0:
    print("Invalid Input")

else:
    print("Reversed Odd Number from {} to 1".format(n))
    if n%2==0:
        n=n-1
    for i in range(n,0,-2):
        print(i)
    else:
        print("-"*50)