#Create a Python program that Compare execution time of summing numbers from 1 to 10 million
#using normal function, threading, and multiprocessing.

import multiprocessing
import time
import threading

def sum():
    s=0
    for i in range(1,10000001):
        s=s+i
    return s

def main():

    start_time = time.time()
    ret1=0
    ret1=t1=threading.Thread(target=sum)
    t1.start()
    t1.join()
    end_time = time.time()
    print("sum of 1 to 10million is : ",ret1)
    print("Execution time of thread is : ",end_time - start_time)


    start_time = time.time()
    ret2=0
    t2=multiprocessing.Pool()
    ret2=t2.apply(sum)
    t2.close()
    t1.join()
    end_time = time.time()
    print("sum of 1 to 10million is : ",ret2)
    print("Execution time of multiprocessing is : ",end_time - start_time)

    start_time = time.time()
    ret3=sum()
    end_time = time.time()
    print("sum of 1 to 10million is : ",ret3)
    print("Execution time of function is : ",end_time - start_time)

if __name__=="__main__":
    main()