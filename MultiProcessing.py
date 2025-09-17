# MultiProcessing

from multiprocessing import Process,Value,freeze_support
def add_num(num1):
    num1.value+=19
    print("the number after ten is: ",num1.value)
if __name__=="__main__":
    freeze_support()
    
    num=Value('i',10)
    print("the intial number is: ",num.value)
    p=Process(target=add_num,args=(num,))
    p.start()
    p.join()
    print("the fianl number : ",num.value)
  