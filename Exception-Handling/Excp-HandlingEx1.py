#Program for Demonstrating Exception Occurrence
#Excp-HandlingEx1.py
print("Program Execution Started")
a=input("Enter First value:")
b=input("Enter Second value:")
x=int(a) #Exception Generated stmt---ValueError
y=int(b) #Exception Generated stmt---ValueError
print("\tFirst Value={}".format(x))
print("\tSecond Value={}".format(y))
z=x/y    #Exception Generated stmt---ZeroDivisionError
print("\tDiv={}".format(z))
print("Program Execution Ended")