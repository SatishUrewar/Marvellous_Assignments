#Accept a number from the user and check whether it is prime or not.

def prime(v1):
        if(v1<2):
         return False
        
        for i in range(2,v1):
            if(v1%i==0):
             return False
        return True    
def main():
    a=int(input("Enter number : "))
    ans=prime(a)
    if(ans==True):
        print(a," is a prime number.")
    else:
        print(a," is a not prime number.")
       
if __name__=="__main__":
    main()