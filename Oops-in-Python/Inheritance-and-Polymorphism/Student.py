#Student.py

from College import College
from University import University
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