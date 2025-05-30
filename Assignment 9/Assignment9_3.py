#Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a list.

import multiprocessing

def fact(v1):
    ans=1
    for i in range(1,v1+1):
        ans=ans*i
    return ans

def main():
   a=int(input("Enter number element to store : "))
   b=[]
   for i in range(a):
      no=int(input())
      b.append(no)

   result=[]
   t1=multiprocessing.Pool()
   result=t1.map(fact,b)
   t1.close()
   t1.join()
   print("factorial is : ",result)

if __name__=="__main__":
    main()