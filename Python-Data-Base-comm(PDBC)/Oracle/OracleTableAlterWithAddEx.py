#program for Modifying the Column Sizes of Employee Table
#OracleTableAlterWithAddEx.py

import oracledb as orc
def alter_table_add():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
        curobj=conobj.cursor()
        aq="alter table employee add(cname varchar2(10) not null)"
        curobj.execute(aq)
        conobj.commit()
        print("Table Altered Successfully---verify")
    except orc.DatabaseError as err:
        print("Problem in oracle DB:",err)

#main Program
alter_table_add()