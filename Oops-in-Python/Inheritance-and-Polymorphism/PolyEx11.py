# Write a program which will implement the following:
# Let us assume there exists a University. Accept and display university name and location.
# Let us assume there exists a College which contains college name and its location. Accept and display college details along with university details.
# Let us assume there exists a Student which contains student number, name, and course pursued. Accept and display student details along with college and university details.
#PolyEx11.py

class University:
    def get_data(self):
        self.uname=input("enter university name:")
        self.uloc=input("enter university location:")
    def disp_data(self):
        print("----------------------------------------")
        print("University Details")
        print("----------------------------------------")
        print("University Name:",self.uname)
        print("University Location:",self.uloc)
        print("----------------------------------------")
class College(University):
    def get_data(self):
        self.cname=input("enter College Name:")
        self.cloc=input("enter College Location:")
        super().get_data()
    def disp_data(self):
        print("----------------------------------------")
        print("College Details")
        print("----------------------------------------")
        print("College Name:",self.cname)
        print("College Location:",self.cloc)
        print("----------------------------------------")
class Student(College):
    def get_data(self):
        self.sno=input("enter Student Number:")
        self.sname=input("enter Student Name:")
        self.crs=input("enter Student Course:")
        super().get_data()
    def disp_data(self):
        University.disp_data(self)
        College.disp_data(self)
        print("----------------------------------------")
        print("Student Details")
        print("----------------------------------------")
        print("Student Number:",self.sno)
        print("Student Name:",self.sname)
        print("Student Course:",self.crs)
        print("----------------------------------------")

#Main Program
so=Student()
so.get_data()
so.disp_data()
