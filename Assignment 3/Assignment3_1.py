#Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

from functools import reduce
sum=lambda A,B:A+B


def main():
    a=int(input("how many number you want to store : "))
    b=list()
    for i in range(a):
        no=int(input())
        b.append(no)

    result=reduce(sum,b)
    print("your list addition is : ",result)
       
if __name__=="__main__":
    main()


#result=0
    #for i in b:
       #result=result+i
    
