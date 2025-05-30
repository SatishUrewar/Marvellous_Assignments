#3. Design python application which creates two threads as evenlist and oddlist.
# Both the threads accept list of integers as parameter.
# Evenlist thread add all even elements from input list and display the addition.
# Oddlist thread add all odd elements from input list and display the addition.

import threading
def evenlist(v1):
     sum=0
     for i in v1:
         if(i%2==0):
            sum=i+sum
     print("sum of even num in list : ",sum)

def oddfactor(v1):
    sum=0
    for i in v1:
        if(i%2!=0):
            sum=sum+i
    print("sum of odd num in list : ",sum)
    

def main():
    a=int(input("Enter number : "))
    b=[]
    for i in range(a):
        no=int(input())
        b.append(no)
    
    t1=threading.Thread(target=evenlist,args=(b,))
    t1.start()
    t2=threading.Thread(target=oddfactor,args=(b,))
    t2.start()

if __name__=="__main__":
    main()