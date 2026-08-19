#program for Creating the Table-employee in MySQL
#MySQLTableCreateEx.py

#MySQLDataBaseCreate.py
import mysql.connector as mc
def create_table():
    try:
        conobj=mc.connect(host="localhost",
                          user="root",
                          passwd="@4321Raviptdr",
                          use_pure=True,
                          database="batch6pm")
        curobj=conobj.cursor()
        ct="create table jay(eno int primary key, name varchar(15) not null, sal float not null, cname varchar(15) not null)"
        curobj.execute(ct)
        print("Table Created Successfully in MySQL---verify")
    except mc.DatabaseError as e:
        print("Problem in MySQL:",e)
#Main Program
create_table()


"""

show databases;
use database-name;
desc table-name;
select * from table-name

"""