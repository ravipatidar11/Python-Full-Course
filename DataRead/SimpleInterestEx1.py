# Cal Simple interest and Total amount to pay
# SimpleInterestEx1.py

P=float(input("Enter the Principle amount: "))
R=float(input("Enter the Rate of interest: "))
T=float(input("Enter the total Time : "))

#cal of simple interest
smplInt=(P*T*R)/100

#show the Result
print("-"*50)
print("\t\tSimple Interest : ",smplInt)
print("-"*50)
print("Principle Amount : ",P)
print("Rate of Interest : ",R)
print("Total Time : ",T)
print("-"*50)
print("\t\tTotal Amount To Pay :",P+smplInt)
print("-"*50)