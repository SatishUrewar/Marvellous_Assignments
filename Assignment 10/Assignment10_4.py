#Write a program which contains filter(), map() and reduce() in it.
#Python application which contains one list of numbers.
#List contains the numbers which are accepted from user.
#Filter should filter out all such numbers which are even.
#Map function will calculate its square.
#Reduce will return addition of all that numbers.

from functools import reduce

even = lambda X: X%2==0
square = lambda X: X*X
addition = lambda X,Y: X+Y

def main():
    a = int(input("Enter the no you want to take input: "))
    b = []

    for i in range(a):
        no=int(input())
        b.append(no)

    ans1 = list(filter(even, b))
    print("List after filter",ans1)

    ans2 = list(map(square, ans1))
    print("List after map",ans2)

    ans3 = reduce(addition, ans2)
    print("output of reduce",ans3)

if __name__=="__main__":
    main()