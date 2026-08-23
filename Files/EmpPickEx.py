#Program for Reading employee values from Key Board and save them as Record in file of Secondary Memory
#EmpPickEx.py
import pickle
def saveempdata():
    with open("emp.pick","ab") as fp:
        while(True):
            #Accept Employee Values from KBD
            print("-"*50)
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            print("-" * 50)
            #add emp values to Iterable Object
            lst=list()
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            #Save lst data into the file
            pickle.dump(lst,fp)
            print("Employee Saved Sucessfully--verify")
            print("-" * 50)
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                break
#Main Program
saveempdata()