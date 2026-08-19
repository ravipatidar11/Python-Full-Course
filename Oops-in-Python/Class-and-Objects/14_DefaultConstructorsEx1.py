#ConstructorsEx1.py

class Employee:
    def __init__(self): #Default /Parameter-less Constructor
        print("Iam from Default Constructor")
        print("---------------------------------")
        self.eno=100
        self.name="Ravi"
        print("\tEmployee Number:",self.eno)
        print("\tEmployee Name:",self.name)
        print("----------------------------------")

#Main Program
eo1=Employee() # Object Creation--Makes to PVM to Call Default Constructor Implicitly
eo2=Employee() # Object Creation--Makes to PVM to Call Default Constructor Implicitly
eo3=Employee() # Object Creation--Makes to PVM to Call Default Constructor Implicitly