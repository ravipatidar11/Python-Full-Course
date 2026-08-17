#program for Demonstrating the Concept of continue keyword
#ContinueStmtEx1.py

s="PYTHON"

for ch in s:
    print(ch)
else:
    print("I am from Else part of for loop")
print("-------------------------------------")

#REQ: only print PYT without using Indexing and Slicing

for ch in s:
    if(ch=="H"):
        continue
    print(ch, end="")

else:
    print()
    print("------------------------")

    print("\nI am from Else part of for loop")