#DivOperation.py<---Module Name

from DivExcept1 import NumberDivisionError

def division(a,b):
    if (b==0):
        raise NumberDivisionError
    else:
        return (a/b)

#Phase-2:  Hitting the Programmer-Defined Exception