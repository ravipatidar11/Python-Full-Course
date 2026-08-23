#EmpView.py<-------Module Name
import pickle
def viewSingleEmployee():
    #Get the Employee Records int main memory
    with open("E:\\KVR-PYTHON-9AM\\FILES\\empproj.pick","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        result=False
        eno=int(input("Enter Employee Number to View: "))
        for record in records:
            if(record[0]==eno):
                result=True
                rec=record
                break
        print("----------------------------------------------")
        if(result):
            print("Employee Details:")
            print("\tEmployee Number:{}".format(rec[0]))
            print("\tEmployee Name:{}".format(rec[1]))
            print("\tEmployee Salary:{}".format(rec[2]))
        else:
            print("\tEmployee Record Does Not Exist")
        print("----------------------------------------------")

def viewAllEmployees():
    try:
        with open("E:\\KVR-PYTHON-9AM\\FILES\\empproj.pick","rb") as fp:
            print("-------------------------------------------")
            print("\tENO\t\tNAME\tSALARY")
            print("-------------------------------------------")
            while(True):
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:

                    print("-------------------------------------------")
                    break
    except FileNotFoundError:
        print("File Does not Exist")
