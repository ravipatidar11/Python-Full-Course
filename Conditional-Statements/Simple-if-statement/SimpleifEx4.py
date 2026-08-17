#program for accepting any Digit and Display Its Name
#SimpleifEx4.py

num=int(input("Enter a number: "))

if num==1:
    print("{} is 1".format(num))
if num==2:
    print("{} is 2".format(num))
if num==3:
    print("{} is 3".format(num))
if num==4:
    print("{} is 4".format(num))
if num==5:
    print("{} is 5".format(num))
if num==6:
    print("{} is 6".format(num))
if num==7:
    print("{} is 7.".format(num))
if num==8:
    print("{} is 8".format(num))
if num==9:
    print("{} is 9".format(num))
if num<0 and num in range (-1,-10,-1):
    print("{} is negative digit".format(num))
if num<-9:
    print("{} is negative Number".format(num))
if num>9:
    print("{} is positive Number".format(num))
