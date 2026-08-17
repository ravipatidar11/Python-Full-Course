#Program for Accepting any value and Decide weather It is +VE OR -VE OR Zero
#ElIfElseEx1.py

val=float(input('Enter Any number: '))

if val>0:
    print("{} is +ve".format(val))
elif val<0:
    print("{} is -ve".format(val))
elif val==0:
    print("{} is zero".format(val))

