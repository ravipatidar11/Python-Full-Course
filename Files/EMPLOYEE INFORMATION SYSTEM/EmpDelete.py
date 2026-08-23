#EmpDelete.py<-------Module Name
import pickle
def deleteEmployee():
    # Get the Employee Records int main memory
    with open("E:\\KVR-PYTHON-9AM\\FILES\\empproj.pick", "rb") as fp:
        records = []
        while True:
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # Delete the emnployee record
    res=False
    eno=int(input("Enter Employee Number to Delete:"))
    for index in range(0,len(records)):
        if(records[index][0]==eno):
            res=True
            recind=index
            break
    if(res):
        records.pop(recind)
        #re-write the remaining records into the file
        with open("E:\\KVR-PYTHON-9AM\\FILES\\empproj.pick", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("\tEmployee Record Deleted-verify")
    else:
        print("\tEmployee Record Does not Exist")
