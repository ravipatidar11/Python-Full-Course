#InhProg3.py

class Parent:
    def get_parent_property(self):
        self.pp=float(input("Enter Parent Property:"))
class Child(Parent):
    def get_child_property(self):
        self.cp=float(input("Enter Parent Property"))
    def total_property(self):
        self.tp=self.pp+self.cp
        print("--------------------------------------")
        print("\tParent Property=", self.pp)
        print("\tChild Property=", self.cp)
        print("\tTotal Property=", self.tp)
        print("--------------------------------------")

#Main Program
c=Child()
c.get_parent_property()
c.get_child_property()
c.total_property()