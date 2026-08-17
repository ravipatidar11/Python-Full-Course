#Write a Python program to find the unique element in a list.
#6-UniqueElementInList.py

lst1=list(map(int,input("Enter Elements of List separated by Comma:").split(",")))

for i in lst1:
    if lst1.count(i)==1:
        uq=i

print("Unique Elements in a List:",uq)