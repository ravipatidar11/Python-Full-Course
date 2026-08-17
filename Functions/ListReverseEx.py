#Program for accepting a List of Values and Get Its Reverse using 'Functions'
#without using extended Slicing and reverse()
#ListReverseEx.py

def read_val():
    n=int(input("enter how many elements do you want?:"))
    if n<=0:
        print("invalid input")
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("enter value {} = ".format(i)))
            lst.append(val)
        else:
            print("Original Value is",lst)
    return lst

def reverse_val():
    rv=read_val()
    left=0
    right=len(rv)-1
    while left<right:
        rv[left],rv[right]=rv[right],rv[left]
        left =left+1
        right =right-1
    else:
        print("reversed value is {}".format(rv))

reverse_val()



