#Write a Python program to remove duplicate elements while preserving order
#5-RemoveDuplicates.py

element=input("Enter your Element separated by Space:").split()


"""rdl=set(element)
print(rdl)"""

rde=[]
for i in element:
    if i not in rde:
        rde.append(i)
print(rde)