# Process vs thread:
# Process is an instance of a programm
# Thread is an entity in the process
# All threads in a process share the same memory
# A process can have multiple threads
# Each process has its own memory space
# Threads between them can have race conditions (two threads try to modify the same variable)

# In python each variable has the GIL: its a counter for how many threads references the variable
# When GIL is 0 then the object will be destroied to free memory
# When something goes wrong we can have memory leak (memory does not deallocated) or crash (used variable has been destroied)
# %%
# multiprocessing: run many processes with one thread
from multiprocessing import Process
import os
import time

processes = []
# start processes as much as machine cpu
num_of_processes = os.cpu_count()

def sqare_numbers(a):
    for i in range(100):
        print(i*i)
        time.sleep(1)

# create the processes, pass as target the function to run and a tuple of the args
for i in range(num_of_processes):
    p = Process(target=sqare_numbers, args=(5,))
    processes.append(p)

# start the processes
for p in processes:
    p.start()

# join them for the main thread of the programm to wait until all processes finish
for p in processes:
    p.join()


print("End of all processes")
# %%
# Multithreading: python does not execute the threads in parrallel
#                 to execute in parrallel use multiprocessing of other libraries
# Threads can see the same variables and exchange data
from threading import Thread


threads = []
# start processes as much as machine cpu
num_of_threads = 10


# create the processes, pass as target the function to run and a tuple of the args
for i in range(num_of_threads):
    t = Thread(target=sqare_numbers, args=(5,))
    threads.append(t)

# start the processes
for t in threads:
    t.start()

# join them for the main thread of the programm to wait until all processes finish
for t in threads:
    t.join()
# %%
