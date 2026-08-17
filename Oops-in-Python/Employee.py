#17_Employee.py

class Employee:
    def __init__(self,eno,name,sal):
        self.eno=eno
        self.name=name
        self.sal=sal
    def disp_emp_data(self):
        print("\t{}\t\t{}\t{}".format(self.eno,self.name,self.sal))
