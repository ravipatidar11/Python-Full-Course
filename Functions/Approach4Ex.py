#program for Defining a Function for adding Two Values
#INPUT          : Taking Input Function Body
#PROCESS        : Processing Done in Function Body
#RESULT         : Result Given Back to Function Call (Main Program)
#Approach4Ex.py

def addop():
    a=float(input('Enter first number: '))
    b=float(input('Enter second number: '))
    c=a+b
    return a,b,c

#Main Program
p,q,r=addop() #Multi line Assignment
print("sum ({},{}) = {}".format(p,q,r))
print("----------------------------------------")
#Single line Assignment
res = addop()
print("sum ({},{}) = {}".format(res[0],res[1],res[2]))