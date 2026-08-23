#Program for Showing Internal Flow of Sub Threads  along with Default Thread -MainThread
#SubThreadsInternalFlow.py

import threading
def welcome():
	print("\twelcome() Executed By:",threading.current_thread().name)
def hello():
	print("\thello() Executed By:",threading.current_thread().name)
def hi():
	print("\thi() Executed By:",threading.current_thread().name)
#Main Program
print("Program Execution Started:",threading.current_thread().name)
#Create THREE Sub Threads for executing THREE Functions
t1=threading.Thread(target=welcome)#Here t1 is  Called Sub Thread Object whose default name is thread-1
t2=threading.Thread(target=hello) #Here t2 is  Called Sub Thread Object whose default name is thread-2
t3=threading.Thread(target=hi)  #Here t2 is  Called Sub Thread Object whose default name is thread-3
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
#Join the threads
t1.join()
t2.join()
t3.join()
print("Program Execution Ended:",threading.current_thread().name)