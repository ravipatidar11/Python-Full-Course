#Program for accepting a Line of Text and Find Number chars without spaces
#ForLoopEx10.py

n=input("Enter Line of Text: ")
print("Line of Text and Number chars without spaces: ",n)
l=0
nsp=0
for i in n:
    if not  i.isspace():
        l=l+1
    else:
        nsp = nsp + 1
else:
    print("Given String: ",n)
    print("String without spaces: ",l)
    print("num of space: ",nsp)