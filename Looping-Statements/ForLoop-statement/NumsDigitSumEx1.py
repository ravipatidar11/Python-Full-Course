#program for accepting a Number and Find Its Digits Sum
#NumsDigitsSumEx1.py

num=int(input("Enter Any Number: "))
if(num<=0):
    print("\t{} is Invalid Input".format(num))
else:
    s=0
    for d in str(num):
        s=s+float(d)
    else:
        print("Sum_of_Digits({})={}".format(num,s)) 