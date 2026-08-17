#program for Deleting the Record Based on Employee Number
#OracleRecordDeleteEx1.py

import oracledb as orc
def record_delete():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
        curobj=conobj.cursor()

        empno=int(input("Enter Employee Number for Delete:"))

        dq="delete from employee where sno=%d" %(empno)
        curobj.execute(dq)
        conobj.commit()
        if (curobj.rowcount>0):
            print("{} Record Delete Successfully---verify".format(curobj.rowcount))
        else:
            print("Record Does not Exist")
    except orc.DatabaseError as err:
        print("Problem in Oracle DB:", err)
# main Program
record_delete()