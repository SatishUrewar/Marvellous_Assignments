#Create a python program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second.
#Use threading.Thread

import time
import threading

def thread():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def main():
    t1=threading.Thread(target=thread)
    t1.start()
    t1.join()
    t2=threading.Thread(target=thread)
    t2.start()
    t2.join()
    t3=threading.Thread(target=thread)
    t3.start()
    t3.join()


if __name__=="__main__":
    main()