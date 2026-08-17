#OracleSelectMetaDataEx.py
#program for reading the Col Names
import oracledb as orc

def records_select():
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
        curobj=conobj.cursor()
        # Get the Records from employee table
        sq="select * from employee"
        curobj.execute(sq)
        # Get the Col names from cursor object

        for colinfo in curobj.description:
            print("\t{}".format(colinfo[0]),end="\t")
        print()


    except orc.DatabaseError as e:
        print("Problem in Oracle DB:",e)

#Main Program
records_select()