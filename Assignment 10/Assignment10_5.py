#Write a program which contains filter(), map() and reduce() in it.
#Python application which contains one list of numbers.
#List contains the numbers which are accepted from user.
#Filter should filter out all prime numbers.
#Map function will multiply each number by 2.
#Reduce will return maximum number from that numbers.

from functools import reduce

multi=lambda X: X*2
maximum=lambda X,Y: X if X>Y else Y

def prime(X):
    if X < 2:
        return False
    for i in range(2,X):
     if (X % i==0):
        return  False
    return True

def main():
    a = int(input("Enter the no you want to take input: "))
    b = []
    for i in range(a):
        no = int(input())
        b.append(no)

    ans1 = list(filter(prime,b))
    print("List after filter: ",ans1)

    ans2 = list(map(multi,ans1))
    print("List after map: ",ans2)

    ans3 = reduce(maximum, ans2)
    print("Output of reduce: ",ans3)

if __name__=="__main__":
    main()