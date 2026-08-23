#EmpSearch.py<----Module Name
import pickle
def searchEmployee():
    # get all the records for Viewing single Employee Details Based on ENO
    records=[]
    with open("empproj.data","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break

    empno=int(input("Enter Employee Number for Update: "))
    found=False
    for record in records:
        if (record[0]==empno):
            rec=record
            found=True
            break
    print("-" * 50)
    if (found):
        print("\tValid Employee")
    else:
        print("\tInvalid Employee")
    print("-" * 50)