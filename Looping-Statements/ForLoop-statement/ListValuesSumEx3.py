#program for accepting List of Values and Find their sum
#ListValuesSumEx3.py

n=int(input("Enter Values of List: "))
if n<=0:
    print("Invalid input")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Value {} = ".format(i)))
        lst.append(val)
    else:
        print("List of Values: ",lst)
        s=0
        for val in lst:
            s=s+val
        else:
            print("Sum of List Values: ",s)
            print("AVG of List Values: ",s/len(lst))

