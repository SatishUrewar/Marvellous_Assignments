#Write a program which contains filter(), map() and reduce() in it.
#Python application which contains one list of numbers.
#List contains the numbers which are accepted from user. 
#Filter should filter out all such numbers which are even.
#Map function will calculate its square. 
#Reduce will return addition of all that numbers. 

from functools import reduce

def FilterEven(X):
    return X%2==0

def MapSquare(X):
    return X*X

def ReduceSum(X,Y):
    return X+Y


def main():
    a=int(input("Enter the number that you want to store in list : "))
    b=[]
    for i in range(a):
        num=int(input())
        b.append(num)
    print("User input list : ",b)

    #result1=list(filter(FilterEven,b))
    result1=list(filter(lambda X: X%2==0,b))
    print("Filtered List : ",result1)

    #result2=list(map(MapSquare,result1))
    result2=list(map(lambda X: X*X,result1))
    print("Mapped List : ",result2)

    if result2:
        #result3=reduce(ReduceSum,result2)
        result3=reduce(lambda X,Y: X+Y,result2)
        print("Reduced List : ",result3)
    else:
        print("Can't Reduced an empty list ")


if __name__=="__main__":
    main()