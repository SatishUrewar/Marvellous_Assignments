#Write a program which contains filter(), map() and reduce() in it.
#Python application which contains one list of numbers.
#List contains the numbers which are accepted from user.
#Filter should filter out all prime numbers.
#Map funtion will multiply each number by.
#Reduce will return Maximum number from that number.

from functools import reduce

def FilterPrime(X):
    if X<2:
        return False
    for i in range(2,X):
        if X%i==0:
            return False
    return True

def MapMulti(X):
    return X*2

def ReduceMax(X,Y):
    if X>Y:
        return X
    else:
        return Y


def main():
    a=int(input("Enter the numbers you want to store : "))
    b=[]
    for i in range(a):
        num=int(input())
        b.append(num)
    print("User input list : ",b)

    #result1=list(filter(FilterPrime,b))
    result1=list(filter(lambda X: FilterPrime(X), b))
    print("Filtered List : ",result1)

    #result2=list(map(MapMulti,result1))
    result2=list(map(lambda X:MapMulti(X),result1))
    print("Mapped List : ",result2)

    if result2:
        #result3=reduce(ReduceMax,result2)
        result3=reduce(lambda X,Y:X if X>Y else Y,result2)
        print("Reduced list : ",result3)
    else:
        print("Can't reduce an empty list")


if __name__=="__main__":
    main()