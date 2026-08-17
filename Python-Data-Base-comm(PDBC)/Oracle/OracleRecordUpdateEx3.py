#Program for Updating Emp Sal, Emp Comp Name of Employee table
#Based on Employee Number
#OracleRecordUpdateEx3.py

import oracledb as orc
def record_update():
    while(True):
        try:
            conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl")
            curobj=conobj.cursor()

            empno=int(input("Enter Employee Number for Update:"))
            newempname=input("Enter Employee New Name:")
            newemsal=float(input("Enter Employee New Salary:"))
            newempcompname=input("Enter Employee New Company Name:")

            uq="update employee set sal=%f,name='%s',cname='%s' where sno=%d" %(newemsal,newempname,newempcompname,empno)
            curobj.execute(uq)
            conobj.commit()
            if (curobj.rowcount>0):
                print("{} Record Updated Successfully---verify".format(curobj.rowcount))
            else:
                print("Record Does not Exist")
            print("--------------------------------------------------------------------")
            ch=input("Would you like to Update another record? (yes/no):")
            if ch.lower()=="no":
                print("Thx for using this Program")
                break
        except orc.DatabaseError as err:
            print("Problem in Oracle DB:", err)
# main Program
record_update()
