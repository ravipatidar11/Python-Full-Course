#program for accepting List of Values and Find their sum
#ListValuesSumEx2.py

n=int(input("Enter List of value: "))
if n<0:
    print("Invalid Input")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Value {} = ".format(i)))
        lst.append(val)
    else:
        print("-" * 50)
        print("List of Values =", lst)
        print("-" * 50)
        s=0
        for val in lst:
            s=s+val
        else:
            print("Sum of List Values =", s)
            print("-" * 50)
            print("AVG of List Values =", s/len(lst))
            print("-" * 50)


