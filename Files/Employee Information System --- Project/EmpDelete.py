#EmpDelete.py<--Module Name
import pickle
def deleteEmployee():
    # get all the records for Viewing single Employee Deatils Based on ENO
    records=[]
    with open("empproj.data","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # Get Employee Number for Removing the Record
    found = False
    empno=int(input("Enter Employee Number to Delete: "))
    print("-" * 50)
    for record in records:
        if (record[0]==empno):
            rec=record
            found=True
            break
    if (found):
        records.remove(rec)
        # Re-write the Remaining Records to File after delete
        with open("empproj.data","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
            print("\t Record Deleted Successfully---Verify")
    else:
        print("\tEmployee Number Not Found")
    print("-" * 50)





