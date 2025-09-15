# Dining philosopher problems

import threading
import time
n = int(input("Enter the Number of Phiosophers: "))
chop_stick=[threading.Semaphore(1) for i in range(n)]
def philospher(i):
    print(f"philospher {i+1} is thinking")
    time.sleep(1)
    print(f"philospher {i+1} is hungry")
    time.sleep(1)
    chop_stick[i].acquire()
    chop_stick[(i+1)%n].acquire()
    print(f" philospher {i+1} is eating")
    time.sleep(2)
    chop_stick[i].release()
    chop_stick[(i+1)%n].release()
    print(f"the philospher{i+1} completed eating")
    
    
    
threads=[]
for i in range(n):
    t=threading.Thread(target=philospher,args=(i,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()