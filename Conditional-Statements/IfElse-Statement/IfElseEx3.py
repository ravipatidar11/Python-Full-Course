#Program for Cal simple interest with all data validations
#IfElseEx3.py

p=float(input("Enter Principle Amount: "))
t=float(input("Enter Time: "))
r=float(input("Enter Rate of Interest: "))

if p>0 and t>0 and r>0:
    si=(p*t*r)/100
    print("-"*50)
    print("The principle amount is: ",p)
    print("The Rate of Interest is: ",r)
    print("The Time is: ",t)
    print("-"*50)
    print("\t\tThe Simple Interest is: ",si)
    print("-"*50)
else:
    if p<=0:
        print("\t\t**Invalid Principle Amount**")
    if t<=0:
        print("\t\t**Invalid Time**")
    if r<=0:
        print("\t\t**Invalid Rate of Interest**")
print("Program Execution completed")