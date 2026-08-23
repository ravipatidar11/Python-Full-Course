#Program for Showing Internal Flow of Default Thread -MainThread
#DefaultThreadInternalFlow.py

import threading
def welcome():
    print("\twelcome() Executed By:",threading.current_thread().name)
def hello():
    print("\thello() Executed By:",threading.current_thread().name)
def hi():
    print("\thi() Executed By:",threading.current_thread().name)

#Main Program
print("Program Execution Started:",threading.current_thread().name)
print("-------------------------------")
welcome()
print("-------------------------------")
hello()
print("-------------------------------")
hi()
print("-------------------------------")
print("Program Execution Ending:",threading.current_thread().name)