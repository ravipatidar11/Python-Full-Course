#program for Demonstrating the Functionality of break
#BreakStmtEx2.py
s="PYTHON"
i=0
while(i<+len(s)):
    print(s[i], end="")
    i=i+1
print("\n---------------------------")
# REQ: only print PYT without using Indexing and Slicing
i=0
while(i<=len(s)):
    if (s[i]=="H"):
        i=i+1
        break
    print(s[i], end="")
    i = i + 1
else:
    print()
    print("I am from Else pert of while loop")