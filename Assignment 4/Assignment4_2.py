#Write a program which contains one lambda function which accepts two parameters and return its multiplication.

#def multi(x,y):
#    return x*y
multi=lambda x,y:x*y

def main():
    num1=int(input("Enter 1st number : "))
    num2=int(input("Enter 2nd number : "))

    result=multi(num1,num2)

    print("Mutiplication of two num is : ",result)


if __name__=="__main__":
    main()