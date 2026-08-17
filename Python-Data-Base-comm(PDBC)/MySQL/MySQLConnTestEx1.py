#MySQLConnTestEx1.py

import mysql.connector as mc
try:
    conobj=mc.connect(host="127.0.0.1",
                      user="root",
                      passwd="@4321Raviptdr",
                      use_pure=True)
    print("Python Program Got Connection to MySQL")
except mc.DatabaseError as e:
    print("Problem in MySQL:",e)