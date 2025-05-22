#Accept a number and print its factorial using a for loop.

def Fact(X):
    ans = 1
    for i in range(1,X+1):
        ans=ans*i
    print("Factorial of ",X,"is : ",ans)

def main():
    num=int(input("Enter a number : "))
    Fact(num)


if __name__=="__main__":
    main()