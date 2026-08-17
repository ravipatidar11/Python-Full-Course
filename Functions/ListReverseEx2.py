#Program for accepting a List of Values and Get Its Reverse (String Values)
#without using extended Slicing and reverse()
#ListReverseEx2.py

n=int(input("Enter number of list u want :"))
if n<=0:
    print("Invalid Input")
else:
    lst=[]
    for i in range(1,n+1):
        val=(input("enter value {} = ".format(i)))
        lst.append(val)
    print("Original Val =",lst)

    lst1=lst
    left = 0
    right = len(lst)-1
    while left < right:
        lst1[left],lst1[right]=lst1[right],lst1[left]
        left+=1
        right-=1
    else:
        print("Reverse Val = ",lst1)
