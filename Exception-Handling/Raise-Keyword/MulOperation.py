# MulOperation.py <----- Module Name

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

