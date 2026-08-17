#Program for Creating a Table Employee
#OracleTableCreateEx.py
import oracledb as orc
def create_table(): #Step-1
    try:
        conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl") #Step-2
        curobj=conobj.cursor() #Step-3
        tc="create table employee(Eno number(5) primary key, name varchar2(10) not null, sal number(5,2) not null, cname varchar2(10))"
        curobj.execute(tc)
        conobj.commit()
        print("Table Created Successfully---Verify")#Step-4

    except orc.DatabaseError as err:
        print("Problem in oracle DB:",err)

#main program
create_table()