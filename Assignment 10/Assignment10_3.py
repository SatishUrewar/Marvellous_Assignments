#Write a program which contains filter(), map() and reduce() in it.
#Python application which contains one list of numbers.
#List contains the numbers which are accepted from user.
#Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
#Map function will increase each number by 10.
#Reduce will return product of all that numbers.

from functools import reduce

product = lambda X, Y: X*Y
FData = lambda X: X >=70 and X<=90
MData = lambda X: X+10

def main():
    a = int(input("Enter the no you want to take input: "))
    b = []
    for i in range(a):
        no = int(input())
        b.append(no)

    ans1=list(filter(FData,b))
    print("List after filter: ",ans1)

    ans2=list(map(MData,ans1))
    print("List after Map: ",ans2)

    ans3=reduce(product,ans2)
    print("Output of reduce: ",ans3)

if __name__=="__main__":
    main()