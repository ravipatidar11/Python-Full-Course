#program for Creating Database on the name of batch6pm
#MySQLDataBaseCreate.py
import mysql.connector as mc
def create_db():
    try:
        conobj=mc.connect(host="127.0.0.1",
                          user="root",
                          passwd="@4321Raviptdr",
                          use_pure=True)
        curobj=conobj.cursor()
        cd="create database batch6pm"
        curobj.execute(cd)
        print("Database Created in MySQL---verify")
    except mc.DatabaseError as e:
        print("Problem in MySQL:",e)
#Main Program
create_db()