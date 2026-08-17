#Program for accepting a List of Values and Get Its Reverse (Float Values)
#using extended Slicing
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
    return lst

def reverse_val():
    rv=read_val()
    rv1=rv[::-1]
    print("Original Value is {}".format(rv))
    print("reversed value is {}".format(rv1))

reverse_val()