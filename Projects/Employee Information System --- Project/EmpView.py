import pickle

def viewSingleEmployee():
    #get all the records for Viewing single Employee Details Based on ENO
    records=[]
    with open("empproj.data","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    empno=int(input("Enter Employee Number: "))
    found=False
    for record in records:
        if (record[0]==empno):
            rec=record
            found=True
            break
    print("--------------------------------------------------")
    if (found):
        print("\tEmployee Number: {}".format(rec[0]))
        print("\tEmployee Name: {}".format(rec[1]))
        print("\tEmployee Salary: {}".format(rec[2]))


def viewAllEmployee():
    with open("empproj.data","rb") as fp:
        print("---------------------------------------")
        print("\tEno\t\tName\t\tSalary")
        print("---------------------------------------")
        while(True):
            try:
                records=pickle.load(fp)
                for val in records:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("--------------------------------")
                break


