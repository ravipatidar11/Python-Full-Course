#Program for Demonstrating Exception Occurrence
#Excp-HandlingEx6.py ----- single exception at a time with default except block
try:
    print("Program Execution Started")
    a=input("Enter First value:")
    b=input("Enter Second value:")
    x=int(a) #Exception Generated stmt---ValueError
    y=int(b) #Exception Generated stmt---ValueError
    z=x/y    #Exception Generated stmt---ZeroDivisionError
except ValueError as rv:
    print("\tDon't use STR,ALNUM,and SYMBOLS:",rv)
except ZeroDivisionError as rv:
    print("\tDon't use Zero for denominator:",rv)
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