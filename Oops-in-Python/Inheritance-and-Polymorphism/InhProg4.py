#InhProg4.py

class Parent:
    def get_parent_property(self):
        self.pp=float(input("Enter Parent Property:"))
class Child(Parent):
    def get_child_property(self):
        self.cp=float(input("Enter Parent Property"))
    def total_property(self):
        self.get_parent_property()
        self.get_child_property()
        self.tp=self.pp+self.cp
        print("--------------------------------------")
        print("\tParent Property=", self.pp)
        print("\tChild Property=", self.cp)
        print("\tTotal Property=", self.tp)
        print("--------------------------------------")

#Main Program
c=Child()
c.total_property()