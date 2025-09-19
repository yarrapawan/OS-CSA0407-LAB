# Process Synchronization 

import threading
import time
import random


balance = 100
mutex = threading.Lock()   


def deposit(amount):
    global balance
    for _ in range(5):
        time.sleep(random.uniform(0.2, 0.6))  
        mutex.acquire()      
        print(f"[{threading.current_thread().name}] Depositing {amount}")
        balance_before = balance
        balance = balance_before + amount
        print(f"Balance updated: {balance_before} -> {balance}")
        mutex.release()       


def withdraw(amount):
    global balance
    for _ in range(5):
        time.sleep(random.uniform(0.2, 0.6)) 
        mutex.acquire()       
        if balance >= amount:
            print(f"[{threading.current_thread().name}] Withdrawing {amount}")
            balance_before = balance
            balance = balance_before - amount
            print(f"Balance updated: {balance_before} -> {balance}")
        else:
            print(f"[{threading.current_thread().name}] Withdrawal of {amount} FAILED (Insufficient funds)")
        mutex.release()       


t1 = threading.Thread(target=deposit, args=(50,), name="Producer")
t2 = threading.Thread(target=withdraw, args=(30,), name="Consumer")

t1.start()
t2.start()

t1.join()
t2.join()

print("\nFinal Balance:", balance)