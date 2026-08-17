# MulOperationDemoAllAtOnce.py

class NegativeNumberError(Exception):pass
class ZeroError(BaseException):pass


from MulExcept import NegativeNumberError,ZeroError

def table(n):
    n=int(n)  #here we convert str int into int--Possibility of raising ValueError
    if (n<0):
        raise NegativeNumberError
    elif (n==0):
        raise ZeroError
    else:
        print("-"*50)
        print("Mul Table of",n)
        print("-" * 50)
        for i in range(1,11):
            print("\t{} x {} = {}".format(n,i,n*i))
        print("-" * 50)


#Main Program

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