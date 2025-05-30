#1.Design python application which creates two thread named as even and odd.
#Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.

import threading

def Even():
    for i in range(2,21,2):
        print("even numbers :",i)

def odd():
    for i in range(1,20,2):
        print("Odd number : ",i)

def main():
    t1=threading.Thread(target=Even)
    t1.start()
    t2=threading.Thread(target=odd)
    t2.start()

if __name__=="__main__":
    main()