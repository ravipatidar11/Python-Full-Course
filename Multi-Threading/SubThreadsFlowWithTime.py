#Program for Showing the Execution time of Sub Threads along with  MainThread
#SubThreadsFlowWithTime.py

import threading,time
def squares(lst):
    for val in lst:
        print("\t{}--->Square({})={}".format(threading.current_thread().name,val,val**2))

def cubes(lst):
    for val in lst:
        print("\t{}--->Cubes({})={}".format(threading.current_thread().name, val, val ** 3))

#Main Program
bt=time.time()
print("Program Execution Started:",threading.current_thread().name)
lst=[10,12,4,15,16,17,19,23,24]
#Create a Sub Thread for executing squares() and cubes()
t1=threading.Thread(target=squares,args=(lst,))
t2=threading.Thread(target=cubes,args=(lst,))
#Dispatch the sub threads
t1.start()
t2.start()
#Join the Sub Threads
t1.join()
t2.join()
print("Program Execution Finished:",threading.current_thread().name)
et=time.time()
print("Total Execution Time:",bt-et)