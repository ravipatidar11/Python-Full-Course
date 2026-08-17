#Program for Reading List of Values from Key Board
#ListCompHenEx2.py

lst=[float(val) for val in input("Enter List of values Separated by Space: ").split()]
print("Content of List: ",lst)
lst1=0
for val1 in lst:

    lst1 = lst1 + val1

print(lst1)