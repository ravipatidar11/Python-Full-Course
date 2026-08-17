# MulOperation.py <---- Main Program

from MulExcept import NegativeNumberError,ZeroError
from MulOperation import table

while(True):
    try:
        table(input("Enter Any Number:"))
    except ZeroError:
        print("\tDon't Enter ZERO---Try Again")
    except NegativeNumberError:
        print("\tDon't Enter -ve Number---Try Again")
    except ValueError:
        print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS--Try Again")
    else:
        print("Thanx For Using Program")
        break