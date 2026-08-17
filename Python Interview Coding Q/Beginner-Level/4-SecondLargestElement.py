#Write a Python program to find the Second Largest element in a list.
#4-SecondLargestElement.py

lst=list(map(int,input("Enter Element of List Separated by space:").split()))
uniq=list(set(lst))
uniq.sort()
sec_max=uniq[-2]
print(sec_max)
