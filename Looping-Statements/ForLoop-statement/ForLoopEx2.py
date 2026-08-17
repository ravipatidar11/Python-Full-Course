#program for Generating N to 1 where N is +VE
#ForLoopEx2.py

n=int(input("Enter how many number u want: "))

if n<=0:
    print("Invalid input")

else:
    print("Number from {} to 1".format(n))
    for i in range(n,0,-1):
        print(i)
    else:
        print("-"*50)