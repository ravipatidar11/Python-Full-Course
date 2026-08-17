#DivOperationDemo.py<---Main Program
from DivExcept1 import NumberDivisionError
from DivOperation1 import division

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

#Phase-3: Handling the exceptions