#program for Creating Cursor Object
#OracleCursorObjEx.py

import oracledb as orc

conobj=orc.connect("C##RAVI/Ravi123@192.168.1.93:1521/orcl") # Step-2
print("-------------------------------------------------")
print("Python Program Got Connection from Oracle DB")
print("Type of conobj=",type(conobj))
print("-------------------------------------------------")
curobj=conobj.cursor()  # Step-3
print("Pthon Program Created Cursor Object")
print("Type of Curobj=",type(curobj))
print("-------------------------------------------------")