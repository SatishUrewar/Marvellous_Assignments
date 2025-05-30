#2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. 
# Evenfactor thread will display addition of even factors of given number and
# oddfactor will display addition of odd factors of given number. 
# After execution of both the thread gets completed main thread should display message as "exit from main"

import threading
def evenfactor(v1):
     sum=0
     for i in range(1,v1+1):
         if(v1%i==0):
             if(i%2==0):
                 sum=i+sum
     print("sum of even factor : ",sum)

def oddfactor(v1):
    sum=0
    for i in range(1,v1+1):
        if(v1%i==0):
            if(i%2!=0):
                sum=i+sum
    print("sum of odd factor : ",sum)
    

def main():
    a=int(input("Enter number : "))
    t1=threading.Thread(target=evenfactor,args=(a,))
    t1.start()
    t2=threading.Thread(target=oddfactor,args=(a,))
    t2.start()

if __name__=="__main__":
    main()