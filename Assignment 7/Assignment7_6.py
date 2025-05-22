#Write a function that accepts a list of integers and returns a list of prime numbers using filter(). 

def prime(X):
    if(X<2):
        return False
    for i in range(2,X):
        if(X%i==0):
            return False
    return True
    
def main():
    a=int(input("Enter number : "))
    b=[]
    for i in range(a):
     no=int(input())
     b.append(no)

    ans1=list(filter(prime,b))
    
    print("Prime numbers : ",ans1)
      
if __name__=="__main__":
    main()