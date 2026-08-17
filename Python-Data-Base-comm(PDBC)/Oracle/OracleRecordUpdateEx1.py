#Program for Updating Emp Sal, Emp Comp Name of Employee table
#Based on Employee Number
#OracleRecordUpdateEx1.py


import oracledb as orc
def record_update():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
        curobj=conobj.cursor()
        uq="update employee set sal=2.5,cname='NIT' where sno=300"
        curobj.execute(uq)
        conobj.commit()
        if (curobj.rowcount>0):
            print("{} Record Updated Successfully---verify".format(curobj.rowcount))
        else:
            print("Record Does not Exist")
    except orc.DatabaseError as err:
        print("Problem in Oracle DB:", err)
# main Program
record_update()