import threading
import time
import random

buffer = []
buffer_size = 5

empty = threading.Semaphore(buffer_size)  # Count of empty slots
full = threading.Semaphore(0)             # Count of full slots
mutex = threading.Semaphore(1)            # Mutual exclusion

# Producer
def producer():
    for i in range(10):
        empty.acquire()
        mutex.acquire()
        item = random.randint(1, 100)
        buffer.append(item)
        print(f"Produced: {item}")
        mutex.release()
        full.release()
        time.sleep(random.uniform(0.1, 0.5))

# Consumer
def consumer():
    for i in range(10):
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"Consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(random.uniform(0.1, 0.5))

# Threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
print("Producer-Consumer simulation finished.")
