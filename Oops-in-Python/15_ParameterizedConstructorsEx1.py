#ConstructorsEx2.py

class Employee:
    def __init__(self,r,v):
        print("Iam from Parameterized Constructor")
        print("----------------------------------------")
        self.eno=r
        self.name=v
        print("\tEmployee Number:",self.eno)
        print("\tEmployee Name:",self.name)
        print("----------------------------------------")


#Main Program
eo1=Employee(10,20) # Object Creation--Makes to PVM to Call Parameterized Constructor Implicitly
eo2=Employee(100,200) # Object Creation--Makes to PVM to Call Parameterized Constructor Implicitly
eo3=Employee(1000,2000) # Object Creation--Makes to PVM to Call Parameterized Constructor Implicitly