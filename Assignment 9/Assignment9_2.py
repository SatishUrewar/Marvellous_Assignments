#Write a Python program using multiprocessing.
#Process to square a list of numbers using multiple processes.

import multiprocessing

def square(v1):
    sq=0
    ab=[]
    for i in v1:
     sq=i*i
     ab.append(sq)
    
    print("list od square : ",ab)

def main():
   a=int(input("Enter number element to store : "))
   b=[]
   for i in range(a):
      no=int(input())
      b.append(no)
    
   t1=multiprocessing.Process(target=square,args=(b,))
   t1.start()

if __name__=="__main__":
    main()