#Write a Python program to find the largest and smallest elements in a list.
#3-MaxAndMinInList.py
import functools
lst=list(map(int,input("Enter Element of List Separated by space:").split()))


#method-1
max=(functools.reduce(lambda x,y:x if x>y else y,lst))
min=(functools.reduce(lambda x,y:x if x<y else y,lst))

print("Max Number =",max)
print("Min Number =",min)



#method-2
"""lst.sort()
print("Max = ",lst[len(lst)-1])
print("Min = ",lst[0])"""