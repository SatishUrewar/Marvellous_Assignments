#Write a program which contains filter(), map() and reduce() in it.
#Python application which contains one list of numbers.
#List contains the numbers which are accepted from user.
#Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
#Map function will increase each number by 10.
#Reduce will return product of all that number.

from functools import reduce

def filterf(X):
    return X>=70 and X<=90

def mapm(X):
    return X+10

def productp(X,Y):
    return X*Y


def main():
    a=int(input("Enter the number that you want to store in list : "))
    b=[]
    for i in range(a):
        num=int(input())
        b.append(num)
    print("User input list : ",b)

    #result1=list(filter(filterf,b))
    result1=list(filter(lambda X:X>=70 and X<=90,b))
    print("Filtered List : ",result1)

    #result2=list(map(mapm,result1))
    result2=list(map(lambda X: X+10,result1))
    print("Mapped List : ",result2)

    if result2:
        #result3=reduce(productp,result2)
        result3=reduce(lambda X,Y:X*Y,result2)
        print("Reduced List : ",result3)
    else:
        print("Can't Reduced an empty list ")


if __name__=="__main__":
    main()