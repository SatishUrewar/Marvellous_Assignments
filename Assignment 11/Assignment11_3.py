#Factorial Using Recursion
#Write a recursive function to calculate factorial of a number.

from functools import reduce

def Addition(no,n1):    
    if (n1==len(no)):
     return 0
    
    current=no[n1]
    rsum=Addition(no,n1+1)
    sum=current+rsum
    return sum
    
    

def main():
    a=[]
    b=input("Enter number : ")
    for i in range(len(b)):
     a.append(int(b[i]))

    ret=Addition(a,0)
    print(ret)
    

if __name__ == "__main__":
    main()