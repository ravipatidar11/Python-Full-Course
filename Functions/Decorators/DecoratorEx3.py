#Program for Cal Square  and Square root of a Given Number By using Decorator
#DecEx3.py--Model-2
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
@square_root      # Internally PVM takes as square_root(square(getval))
@square           # Internally PVM takes as square(getval)
def getval():
    return float(input("Enter a number: "))

#main program
n1,sq1,sqrt1=getval()  #normal Function call
print(n1,sq1,sqrt1)