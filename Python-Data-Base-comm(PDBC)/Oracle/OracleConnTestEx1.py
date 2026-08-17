#Program for Demonstrating Hot to get the connection from oracle db
#OracleConnTestEx1.py
import oracledb as orc #Step-1
try:
    conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl") # Step-2
    print("-------------------------------------------------")
    print("Python Program Got Connection from Oracle DB")
    print("Type of conobj=",type(conobj))
    print("-------------------------------------------------")
except orc.DatabaseError as db:
    print("Problem in Oracle DB:",db)