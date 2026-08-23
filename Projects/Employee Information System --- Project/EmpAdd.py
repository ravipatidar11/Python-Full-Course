#EmpAdd.py<-------Module Name
import pickle

def EmpAdd():
    with open("empproj.data","ab") as fp:
        #Get Employee Values from KWD
        print("----------------------------------------")

        empsno=int(input("Enter Employee Number: "))
        empname=input("Enter Employee Name: ")
        empsal=float(input("Enter Employee Salary: "))

        print("----------------------------------------")

        #Create An Empty List----Iterable Object
        lst=list()
        lst.append(empsno)
        lst.append(empname)
        lst.append(empsal)
        #save the Iterable Object Data into the File
        pickle.dump(lst, fp)
        print("Data Save Successfully---Verify")
        print("----------------------------------------")


