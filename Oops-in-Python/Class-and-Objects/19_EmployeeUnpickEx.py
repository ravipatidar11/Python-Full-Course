#19_EmployeeUnpickEx.py

import pickle

class EmployeeUnpick:
    def read_emp_data(self):
        try:
            with open("emp.pick","rb") as fp:
                while(True):
                    try:
                        emp_records=pickle.load(fp)
                        emp_records.disp_emp_data()
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File does not Exist")

#Main Program
eo=EmployeeUnpick()
eo.read_emp_data()