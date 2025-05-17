#Create a module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for substraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as Number and perform the operation. write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
from Arithmetic import Add,Sub,Mult,Div
def main():

    a1=float(input("enter first number : "))
    a2=float(input("enter 2nd number : "))

    a=Add(a1,a2)
    print("Your addition is : ",a)
    b=Sub(a1,a2)
    print("Your Substraction is : ",b)
    c=Mult(a1,a2)
    print("Your Multiplication : ",c)
    d=Div(a1,a2)
    print("Your division is : ",d)

    



if __name__=="__main__":
    main()
