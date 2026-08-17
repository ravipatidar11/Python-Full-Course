#program for accepting Employee Details from KBD and Insert as Record in Employee Table
#OracleRecordInsertEx1.py

import oracledb as orc
from mysql.connector.aio import cursor


def record_insert():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@localhost:1521/orcl")
        curobj=conobj.cursor()
        iq="insert into employee values(4000,'Rp',15.25,'Medi-caps')"
        curobj.execute(iq)
        conobj.commit()
        print("Record inserted Successfully---verify")
    except orc.DatabaseError as err:
        print("Problem in Oracle DB:", err)


# Main Program
record_insert()