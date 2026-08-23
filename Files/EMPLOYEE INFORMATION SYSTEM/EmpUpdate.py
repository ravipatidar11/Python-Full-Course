#EmpUpdate.py<-------Module Name
import pickle
def updateEmployee():
    # Get the Employee Records int main memory
    with open("E:\\KVR-PYTHON-9AM\\FILES\\empproj.pick", "rb") as fp:
        records = []
        while True:
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
   #Update the salary of emnployee
    print("-------------------------------------------------")
    res=False
    eno=int(input("Enter Employee Number to Update the Salary:"))
    for index in range(0,len(records)):
        if(records[index][0]==eno):
            res=True
            recind=index
            break
    if(res):
        newempsal=float(input("Enter New Employee Salary:"))
        records[recind][2]=newempsal
        #Re-write the Modified record to the file
        with open("E:\\KVR-PYTHON-9AM\\FILES\\empproj.pick", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("\tEmployee Salary Updated--verify")
    else:
        print("Employee Record Does not Exist")
    print("-------------------------------------------------")
