#program for accepting Employee Details from KBD and Insert as Record in Employee Table
#OracleRecordInsertEx3.py

import oracledb as orc


def record_insert():
    while(True):
        try:
            conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
            curobj=conobj.cursor()

            # Accept Employee Details from KBD
            empno=int(input("Enter Employee number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            empcompname=input("Enter Employee Company Name:")

            iq="insert into employee values(%d,'%s',%f,'%s')" %(empno,empname,empsal,empcompname)
            curobj.execute(iq)
            conobj.commit()
            print("{} Record inserted Successfully".format(curobj.rowcount))
            print("-----------------------------------------------------------")
            ch=input("Would you like to insert another record? (yes/no):")
            if ch.lower=="no":
                print("Thx for using this program")
                break
        except orc.DatabaseError as err:
            print("Problem in Oracle DB:", err)


# Main Program
record_insert()