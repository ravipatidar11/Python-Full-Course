#program for Defining a Function for adding Two Values
#INPUT          : Taking Input From Function Call (Main Program)
#PROCESS        : Processing Done in Function Body
#RESULT         : Result Displayed in Function Body
#Approach3Ex.py

def addop(a,b):
    c=a+b
    print("sum ({},{}) = {}".format(a,b,c))

#main function
a=float(input('Enter first number: '))
b=float(input('Enter second number: '))
addop(a,b)