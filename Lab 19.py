import threading
import time
import random

# Shared resource
counter = 0

# Mutex lock
mutex = threading.Lock()

# Number of threads
num_threads = 5

# Thread work simulation
threads = []
for i in range(num_threads):
    t = threading.Thread(target=lambda: (
        mutex.acquire(),
        globals().__setitem__('counter', counter + 1),
        print(f"Thread {i} incremented counter to {counter}"),
        time.sleep(random.uniform(0.1, 0.5)),
        mutex.release()
    ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter value:", counter)
