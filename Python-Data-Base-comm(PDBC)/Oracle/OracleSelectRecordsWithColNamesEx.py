#program for Reading the Records from Table along with Col names
#OracleSelectRecordsWithColNamesEx.py

import oracledb as orc

def records_select():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
        curobj=conobj.cursor()
        # Get the Records from employee table
        sq="select * from employee"
        curobj.execute(sq)
        # Get the Col names from cursor object
        print("--------------------------------------------")
        for colinfo in curobj.description:
            print("\t{}".format(colinfo[0]),end="\t")
        print()
        print("--------------------------------------------")
        # Get the Records
        records=curobj.fetchall()
        if (len(records)==0):
            print("No records Found")
        else:
            for record in records:
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
        print("--------------------------------------------")
    except orc.DatabaseError as e:
        print("Problem in Oracle DB:",e)

#Main Program
records_select()