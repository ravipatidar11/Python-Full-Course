#program for Removing the Table from Oracle DB
#OracleRemoveTable.py

import oracledb as orc
def record_remove():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
        curobj=conobj.cursor()
        rq="drop table employee"
        curobj.execute(rq)
        conobj.commit()
        print("Table Removed Successfully---verify")
    except orc.DatabaseError as err:
        print("Problem in Oracle DB:",err)

#Main Program
record_remove()