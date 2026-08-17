#program for reading the Records from employee--fetchone()
#OracleSelectRecordsEx1.py
import oracledb as orc

def records_select():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
        curobj=conobj.cursor()
        # Get the Records from employee table
        sq="select * from employee"
        curobj.execute(sq)
        # Get the records from cursor object
        while(True):
            record=curobj.fetchone()
            if (record != None):
                for val in record:
                    print("\t{}".format(val),end="\t\t")
                print()
            else:
                break
    except orc.DatabaseError as e:
        print("Problem in Oracle DB:",e)

#Main Program
records_select()