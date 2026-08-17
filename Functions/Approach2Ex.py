#program for Defining a Function for adding Two Values
#INPUT          : Taking Input Function Body
#PROCESS        : Processing Done in Function Body
#RESULT         : Result Displayed in Function Body
#Approach2Ex.py

def addop():
    a=float(input('Enter First number: '))
    b=float(input('Enter Second number: '))
    c=a+b
    print("sum ({},{}) = {}".format(a,b,c))

#main program
addop()