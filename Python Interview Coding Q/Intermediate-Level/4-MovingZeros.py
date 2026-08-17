#Write a Python program to move all zeros to the end of a list.
# #MovingZeros.py

lst=list(map(int,input("Enter Elements of List separated by Comma:").split(",")))

lst1=[]

for i in lst:
    if i==0:
        lst1.append(i)

while 0 in lst:
    lst.remove(0)

lst.extend(lst1)

print(lst)
