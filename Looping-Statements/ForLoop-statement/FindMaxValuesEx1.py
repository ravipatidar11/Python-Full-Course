#program for accepting List of Values and Find  Max Element
#FindMaxValuesEx1.py

n=int(input("Enter List of Values : "))
if n<=0:
    print("Invalid input")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("value {} = ".format(i)))
        lst.append(val)
    else:
        print("-"*50)
        print("List of values=",lst)
        print("-"*50)
        maxvalue=lst[0]
        for i in range(1,n):
            if lst[i]>maxvalue:
                maxvalue=lst[i]
        else:
            print("Maximum value is ",maxvalue)
