# Reader Writter Problem

import threading
import time
import random

# Shared resource
shared_data = 0

# Semaphores
mutex = threading.Semaphore(1)      
rw_mutex = threading.Semaphore(1)   
read_count = 0


def reader(id):
    global read_count, shared_data
    while True:
        time.sleep(random.uniform(0.5, 2))

        # Entry section
        mutex.acquire()
        read_count += 1
        if read_count == 1: 
            rw_mutex.acquire()
        mutex.release()

        
        print(f"Reader {id} is READING: {shared_data}")

    
        mutex.acquire()
        read_count -= 1
        if read_count == 0: 
            rw_mutex.release()
        mutex.release()



def writer(id):
    global shared_data
    while True:
        time.sleep(random.uniform(1, 3))  
        rw_mutex.acquire()  
        shared_data += 1
        print(f"Writer {id} has WRITTEN: {shared_data}")
        rw_mutex.release()


readers = [threading.Thread(target=reader, args=(i,)) for i in range(1, 4)]
writers = [threading.Thread(target=writer, args=(i,)) for i in range(1, 3)]

for t in readers + writers:
    t.start()

# Let it run for some time
time.sleep(10)

print("\nSimulation finished. (You can stop execution manually)")