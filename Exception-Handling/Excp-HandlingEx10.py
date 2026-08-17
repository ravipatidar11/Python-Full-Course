#Program for Demonstrating Exception Occurrence
#Excp-HandlingEx10.py ---- Multiple exception at a time with generic except block
try:
    print("Program Execution Started")
    a=input("Enter First value:")
    b=input("Enter Second value:")
    x=int(a) #Exception Generated stmt---ValueError
    y=int(b) #Exception Generated stmt---ValueError
    z=x/y    #Exception Generated stmt---ZeroDivisionError
except (ValueError,ZeroDivisionError):
    print("\tDon't use STR,ALNUM,and SYMBOLS")
    print("\tDon't use Zero for denominator")
except: #generic except block
    print("Oops Something went Wrong!")
else:
    print("-------------else block---------------")
    print("\tFirst Value={}".format(x))
    print("\tSecond Value={}".format(y))
    print("\tDiv={}".format(z))
finally:
    print("-------------finally block---------------")
    print("Program Execution Ended")