#program for Modifying the Column Sizes of Employee Table
#OracleTableAlterWithModifyEx.py

import oracledb as orc
def alter_table_modify():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
        curobj=conobj.cursor()
        aq="alter table employee modify(sno number(3),name varchar2(15))"
        curobj.execute(aq)
        conobj.commit()
        print("Table Altered Successfully---verify")
    except orc.DatabaseError as err:
        print("Problem in oracle DB:",err)

#main Program
alter_table_modify()