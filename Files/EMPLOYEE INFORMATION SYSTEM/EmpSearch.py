# EmpSearch.py<-------Module Name
import pickle
def searchEmployee():
    # Get the Employee Records int main memory
    with open("E:\\KVR-PYTHON-9AM\\FILES\\empproj.pick", "rb") as fp:
        records = []
        while True:
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        result = False
        eno = int(input("Enter Employee Number to Search: "))
        for index in range(0,len(records)):
            if(records[index][0]==eno):
                result = True
                break
        print("----------------------------------------------")
        if (result):
            print("\tEmployee is Working--Valid")
        else:
            print("\tEmployee is Not working--Invalid")
        print("----------------------------------------------")

