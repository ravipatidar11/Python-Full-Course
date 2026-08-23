#EmpAdd.py<-------Module Name
import pickle
def addEmployee():
    with open("E:\\KVR-PYTHON-9AM\\FILES\\empproj.pick","ab") as fp:
        # Accept Employee Values from KBD
        print("-" * 50)
        empno = int(input("\tEnter Employee Number:"))
        empname = input("\tEnter Employee Name:")
        empsal = float(input("\tEnter Employee Salary:"))
        print("-" * 50)
        # add emp values to Iterable Object
        lst = list()
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        # Save lst data into the file
        pickle.dump(lst, fp)
        print("Employee Record Saved in File Successfully--verify")
        print("-" * 50)

