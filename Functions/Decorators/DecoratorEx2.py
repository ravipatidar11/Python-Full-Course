#Program for Cal Square of a Given Number By using Decorator
#DecEx2.py--Model-2
def square(rv):
    def calculation():
        n=rv()
        res=n**2
        return n,res
    return calculation
@square   # Internally PVM takes as square(getval)
def getval():
    return float(input("Enter a number: "))

#main program
num,result=getval()   #normal function call
print("({})={}".format(num,result))