#18_EmployeePickEx.py

import pickle
from Employee import Employee
class Employee_Pick:
    def get_emp_data(self):
        print("-------------------------------------------")
        self.eno=int(input("Enter Employee number:"))
        self.name=input("Enter Employee Name:")
        self.sal=float(input("Enter Employee Salary:"))
        print("-------------------------------------------")
    def save_emp_data(self):
        with open("emp.pick","ab") as fp:
            eo=Employee(self.eno,self.name,self.sal)
            pickle.dump(eo,fp)
            print("Employee data Saved Successfully---verify")

#Main Program
epo=Employee_Pick()
epo.get_emp_data()
epo.save_emp_data()