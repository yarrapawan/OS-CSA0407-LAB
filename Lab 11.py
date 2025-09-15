# Multi Threading

import threading,time
def print_num():
    for i in range(10-1):
        print(f" num is {i}")
        time.sleep(1)
def print_char():
    for i in ["A","B","C","D","E","F"]:
        print(f"the char is {i}")
        time.sleep(1)
if __name__=="__main__":
    t1=threading.Thread(target=print_num)
    t2=threading.Thread(target=print_char)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Main Threading process is completed")