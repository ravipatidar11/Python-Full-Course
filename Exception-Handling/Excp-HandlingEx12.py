#Program for Demonstrating Exception Occurrence
#Excp-HandlingEx11.py ----- generic except Block with alias name
try:
    print("Program Execution Started")
    a=input("Enter First value:")
    b=input("Enter Second value:")
    x=int(a) #Exception Generated stmt---ValueError
    y=int(b) #Exception Generated stmt---ValueError
    z=x/y    #Exception Generated stmt---ZeroDivisionError
except BaseException as rv: #generic except Block with alias name
    print("Oops Something went Wrong!",rv)
else:
    print("-------------else block---------------")
    print("\tFirst Value={}".format(x))
    print("\tSecond Value={}".format(y))
    print("\tDiv={}".format(z))
finally:
    print("-------------finally block---------------")
    print("Program Execution Ended")