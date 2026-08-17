#Program for Demonstrating global keyword
#GlobalKwdEx2.py

def modify_a_1():
    global a,b
    a=a+1
    b=b+1
def modify_a_2():
    global a,b
    a=a*2
    b=b*2
def access_a():
    # No Need to write global kwd because we are Just accessing Global Variables
    c=a+10
    d=b+10
    print("Value of C =",c)
    print("Value of D =",d)


#Main Program
a,b=10,20 # Here 'a', 'b' are called Global Variables
print("Before Modifying , Value of a={} and b={}".format(a,b))
modify_a_1() # Function Call
print("After Modify1 , Value of a={} and b{}".format(a,b))
modify_a_2() # Function Call
print("After Modify2 , Value of a={} and b{}".format(a,b))
access_a() # Function Call
print("After Accessing , Value of a={} and b{}".format(a,b))