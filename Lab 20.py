import threading
import time
import random

# Shared data
data = 0
read_count = 0

# Semaphores
mutex = threading.Semaphore(1)  # Protect read_count
write = threading.Semaphore(1)  # Writer access

# Number of readers and writers
num_readers = 3
num_writers = 2

threads = []

# Reader threads
for i in range(num_readers):
    t = threading.Thread(target=lambda rid=i: (
        mutex.acquire(),
        globals().__setitem__('read_count', read_count + 1),
        print(f"Reader {rid} started reading, read_count={read_count}"),
        mutex.release(),
        time.sleep(random.uniform(0.5, 1.5)),
        mutex.acquire(),
        globals().__setitem__('read_count', read_count - 1),
        print(f"Reader {rid} finished reading, read_count={read_count}"),
        mutex.release()
    ))
    threads.append(t)
    t.start()

# Writer threads
for i in range(num_writers):
    t = threading.Thread(target=lambda wid=i: (
        write.acquire(),
        globals().__setitem__('data', data + 10),
        print(f"Writer {wid} wrote data={data}"),
        time.sleep(random.uniform(0.5, 1.5)),
        write.release()
    ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final data value:", data)
