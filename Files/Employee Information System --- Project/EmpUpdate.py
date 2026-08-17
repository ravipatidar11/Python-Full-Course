#EmpUpdate.py<--Module Name
import pickle
def updateEmployee():
    # get all the records for Viewing single Employee Details Based on ENO
    records=[]
    with open("empproj.data","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    print("-" * 50)
    empno=int(input("Enter Employee number to Update:"))
    found=False
    for index in range(0,len(records)):
        if (records[index][0]==empno):
            recindex=index
            found=True
            break
    if (found):
        newsal=float(input("Enter Employee New Salary:"))
        records[recindex][2]=newsal
        with open("empproj.data","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmployee Salary Updated---Verify")
    else:
        print("Employee Number Not Found")
    print("-" * 50)
