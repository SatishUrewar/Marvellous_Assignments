#Arithmetic operations on Two numbers
#Write a program to accept two integers from the user and display their:
#sum
#Difference
#Product
#Division

def Sum(n1,n2):
    ans=n1+n2
    return ans

def Difference(n1,n2):
    ans=n1-n2
    return ans

def Product(n1,n2):
    ans=n1*n2
    return ans

def Division(n1,n2):
    ans=n1/n2
    return ans

def main():
    a1=float(input("enter 1st number : "))
    a2=float(input("enter 2nd number : "))

    a=Sum(a1,a2)
    print("Your Sum is : ",a)
    b=Difference(a1,a2)
    print("Your Difference is : ",b)
    c=Product(a1,a2)
    print("Your Product : ",c)
    d=Division(a1,a2)
    print("Your division is : ",d)

if __name__=="__main__":
    main()