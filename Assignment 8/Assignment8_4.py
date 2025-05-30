#4.Design python application which creates three threads as small, capital, digits.
#  All the threads accepts string as parameter.
# Small thread display number of small characters, capital thread display number
# of capital characters and digits thread display number of digits. 
# Display id and name of each thread.
import threading
def small(v1):
    b=[]
    sum=0
    for i in range(len(v1)):
        b.append(v1[i])
    for j in b:
        if(ord(j)>=97) and (ord(j)<=122):
            sum+=1
    print("total small letter : ",sum)

    current_thread=threading.current_thread()
    print("current thread id : ",current_thread.ident)
    print("current thread name : ",current_thread.name)

def capital(v1):
    b=[]
    sum=0
    for i in range(len(v1)):
        b.append(v1[i])
    for j in b:
         if(ord(j)>=65) and (ord(j)<=90):
            sum+=1
    print("total capital letters : ",sum)

    current_thread=threading.current_thread()
    print("current thread id : ",current_thread.ident)
    print("current thread name : ",current_thread.name)
    
def digit(v1):
    b=[]
    sum=0
    for i in range(len(v1)):
        b.append(v1[i])
    for j in b:
         if(ord(j)>=48) and (ord(j)<=57):
            sum+=1
    print("total digit : ",sum)

    current_thread=threading.current_thread()
    print("current thread id : ",current_thread.ident)
    print("current thread name : ",current_thread.name)

def main():
    a=input("enter anything digit or letter : ")
    t1=threading.Thread(target=small,args=(a,))
    t1.start()
    t1.join()
    t2=threading.Thread(target=capital,args=(a,))
    t2.start()
    t2.join()
    t3=threading.Thread(target=digit,args=(a,))
    t3.start()
    t3.join()

if __name__=="__main__":
    main()
