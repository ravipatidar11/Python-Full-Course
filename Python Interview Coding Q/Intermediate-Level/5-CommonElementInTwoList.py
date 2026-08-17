# Write a Python program to find the common elements in two lists.
#5-CommonElementInTwoList.py

lst1=list(map(str,input("Enter Elements of List separated by Comma:").split(",")))
lst2=list(map(str,input("Enter Elements of List separated by Comma:").split(",")))

lst3=[]

for i in lst1:
    for j in lst2:
        if i==j:
            lst3.append(i)
print("Common Elements",lst3)


