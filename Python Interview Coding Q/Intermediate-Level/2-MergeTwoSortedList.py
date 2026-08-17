# Write a Python program to merge two sorted lists into one sorted list.
#2-MergeTwoSortedList.py

lst1=list(map(int,input("Enter list Elements separated by Space:").split()))
lst2=list(map(int,input("Enter list Elements separated by Space:").split()))

lst1.sort()
lst2.sort()

lst1.extend(lst2)
lst1.sort()
print(lst1)