# DivOperation1DemoAllAtOnce.py

class NumberDivisionError(Exception):pass

def division(a,b):
    if (b==0):
        raise NumberDivisionError
    else:
        return (a/b)


#Main Program

while(True):
    try:
        a = float(input("\tEnter First Number: "))
        b = float(input("\tEnter Second Number: "))
        res=division(a,b) #Function Call
    except NumberDivisionError:
        print("\tDON'T ENTER ZERO FOR DEN--try again")
    except ValueError:
        print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS--try again")
    else:
        print("\tDivision({},{})={}".format(a, b, res))
        break
    finally:
        print("I am from Finally Block")
