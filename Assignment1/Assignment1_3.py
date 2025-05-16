#write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Add(num1, num2):
    addition = num1 + num2
    return addition

def main():
    print("Enter the First No : ")
    num1=int(input())
    print("Enter the Second No : ")
    num2=int(input())

    result = Add(num1, num2)
    print("Addition of two no is : ",result)

if __name__=="__main__":
    main()