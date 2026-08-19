#16_DefaultParametrizedConstEx.py

class Employee:
    def __init__(self,k=1,v=2):
        print("Iam from Parameterized Constructor")
        print("----------------------------------------")
        self.eno = k
        self.name = v
        print("\tEmployee Number:", self.eno)
        print("\tEmployee Name:", self.name)    
        print("----------------------------------------")

#Main Program
eo1=Employee() # Object Creation--Makes to PVM to Call Default Constructor Implicitly
eo2=Employee(100,200) # Object Creation--Makes to PVM to Call Parameterized Constructor Implicitly
eo3=Employee(1000,2000) # Object Creation--Makes to PVM to Call Parameterized Constructor Implicitly
eo4=Employee(v=1000) # Object Creation--Makes to PVM to Call Parameterized Constructor Implicitly
eo5=Employee(v=1000,k=2000) # Object Creation--Makes to PVM to Call Parameterized Constructor Implicitly