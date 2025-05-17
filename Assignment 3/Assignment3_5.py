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