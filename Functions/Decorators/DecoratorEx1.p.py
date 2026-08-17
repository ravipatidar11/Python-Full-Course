#Program for Cal Square of a Given Number By using Decorator
#DecEx1.py--Model-1
def square(x):
    def calc():
        n=x()
        res = n**2
        return n,res
    return calc
def getval():
    return float(input("Enter Any Number: "))

#main Program
cal=square(getval)
n1,res1=cal()
print("Given Value is: ",n1)
print("Square of Given Value is: ",res1)