# Write a Python program to check whether a number is an Armstrong number.
#14-ArmstrongNum.py
#num=123,  len(num)=3,  Armstrong=1^3+2^3+3^3=36,    if num==Armstrong,   than the Number is Armstrong


num=int(input("Enter Any Number: "))
temp=num
power=len(str(temp))
sum1=0
while temp>0:   
    digit=temp%10
    sum1=sum1+(digit**power)
    temp=temp//10
print(sum1)
if sum1==num:
    print("{} is an Armstrong Number".format(num))
else:
    print("{} is not an Armstrong Number".format(num))