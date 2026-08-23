#Program for Showing Default Thread Name
#DefaultThreadEx.py

import threading
t_name=threading.current_thread().name
print("Default Thread Name=",t_name)
print("Number Threads=",threading.active_count())

