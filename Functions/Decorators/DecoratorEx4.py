#Program for Cal Square  and Square root of a Given Number By using Decorator
#DecEx4.py--Model-2
def cube(rj):
    def calculation():
        n,sq,sqrt=rj()
        cb=n**3
        return n,sq,sqrt,cb
    return calculation
def square_root(pt):
    def calculation():
        n,sq=pt()
        sqrt=n**0.5
        return n,sq,sqrt
    return calculation
def square(rv):
    def calculation():
        n=rv()
        sq=n**2
        return n,sq
    return calculation
@cube
@square_root
@square
def getval():
    return float(input("Enter a number: "))

#main program
n1,sq1,sqrt1,cb1=getval()
print("Given Num=",n1,"Square=",sq1,"SquareRoot=",sqrt1,"Cube=",cb1)