#program for Defining a Function for adding Two Values
#INPUT          :  Taking Input From Function Call (Main Program)
#PROCESS        :  Processing Done in Function Body
#RESULT         :  Result Given Back to Function Call (Main Program)
#Approach1Ex.py

def addop(a,b):
    c=a+b
    return c

#Main Program
r = float(input("Enter First Number: "))
v = float(input("Enter Second Number: "))
p=addop(r,v)
print("sum ({},{}) = {}".format(r,v,p))