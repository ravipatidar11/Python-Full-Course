#Program for cal Area of Rect with all test cases
#SimpleifEx6.py

l=float(input("Enter Length: "))
b=float(input("Enter Breath: "))

if l>0 and b>0:
    ar=l*b
    print("Area of Rectangle ({},{}) = {}".format(l,b,ar))
if l<=0:
    print("{} Invalid Length".format(l))
if b<=0:
    print("{} Invalid Breath".format(b))