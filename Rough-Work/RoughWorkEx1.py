#Program for accepting a Line of Text and Find Number of chars without spaces
#RoughWorkEx1.py

string=input("Enter a line of text: ")

print("Number of chars without spaces")
l=0
nsp=0
for i in string:
    if not i.isspace():
        l=l+1
    else:
        nsp=nsp+1
else:
    print("---------------------------------")
    print("Number of chars without spaces:" ,l)
    print("Number of spaces:" ,nsp)
    print("----------------------------------")
