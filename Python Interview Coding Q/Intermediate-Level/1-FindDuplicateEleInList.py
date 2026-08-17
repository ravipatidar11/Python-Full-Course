#Write a Python program to find duplicate elements in a list.
#FindDuplicateEleInList.py

lst=list(map(int,input("Enter list element separated by space:").split()))

duplicate = []

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j] and lst[i] not in duplicate:
            duplicate.append(lst[i])
if duplicate:
    print("Duplicate Elements =",duplicate)
else:
    print("No Duplicates Elements")