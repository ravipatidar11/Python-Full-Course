#program for Demonstrating the Functionality of break
#BreakStmtEx3.py

s="MISSISSIPPI"

for ch in s:
    print(ch)
else:
    print("\n--------------------------------------")
    print("I am from Else part of for loop")
print("--------------------------------------")
#REQ: only print PYT without using Indexing and Slicing
i=0
for ch in s:
    if(ch=="I"):
        i=i+1
        if (i==2):
            break
    print("\t",ch, end="")
print("\n--------------------------------------")
print("\nI am from Else part of for loop")