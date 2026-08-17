#Program for Accepting any value and Decide weather It is +VE OR -VE OR Zero
#IfElseEx2.py

val=float(input("Enter any value: "))

if val>0:
    print("{} is +ve".format(val))
else:
    if val<0:
        print("{} is -ve".format(val))
    else:
        print("{} is Zero".format(val))

