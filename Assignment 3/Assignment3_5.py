#Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as Marvellous Num. Name of the function from main python file should be ListPrime().
from functools import reduce
from MarvellousNum import ChkPrime,sum



def Listprime():

    a=int(input("Enter how many num u want to store : "))
    b=list()
    for i in range (a):
        no=int(input())
        b.append(no)
    
    data=list(filter(ChkPrime,b))
    
    result=reduce(sum,data)
    print("prime numbers are : ",data)
    print("The Total prime number addition is : ",result)
    

    
    

if __name__=="__main__":
 Listprime()
