#Program for Demonstrating global keyword
#GlobalKwdEx1.py

def modify1():
    global a
    a=a+1
def modify2():
    global a
    a=a*2

#Main Program
a=10
print("Value of a Before Modifying: ",a) #a=10
modify1()
print("Value of a After Modify1: ",a) #a=11
modify2()
print("Value of a After Modify2: ",a) #a=22
