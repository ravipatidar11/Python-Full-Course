#Program for Demonstrating Exception Occurrence
#Excp-HandlingEx5.py ----- Default except Block
try:
    print("Program Execution Started")
    a=input("Enter First value:")
    b=input("Enter Second value:")
    x=int(a) #Exception Generated stmt---ValueError
    y=int(b) #Exception Generated stmt---ValueError
    z=x/y    #Exception Generated stmt---ZeroDivisionError
except: #Default except Block
    print("Oops Something went Wrong!")
else:
    print("-------------else block---------------")
    print("\tFirst Value={}".format(x))
    print("\tSecond Value={}".format(y))
    print("\tDiv={}".format(z))
finally:
    print("-------------finally block---------------")
    print("Program Execution Ended")