#Program for Showing the Execution time of Default Thread-MainThread
#DefaultThreadFlowWithTime.py

import threading, time

def squares(lst):
    for val in lst:
        print("\t{}--->Square({})".format(threading.current_thread().name,val,val**2))

def cubes(lst):
    for val in lst:
        print("\t{}--->Square({})".format(threading.current_thread().name, val, val ** 3))

#Main Program
bt=time.time()
print("Program Execution Started:",threading.current_thread().name)
lst=[10,12,4,15,16,17,19,23,24]
squares(lst) #Function call
print("---------------------------------------------------------------")
cubes(lst) #Function call
print("---------------------------------------------------------------")
print("Program Execution Ended:",threading.current_thread().name)
et=time.time()
print("Total Execution Time of Default Thread:",et-bt)