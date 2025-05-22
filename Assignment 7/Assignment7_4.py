#Accept a list of numbers and use reduce() (from functools) to find the product of all numbers.
 
from functools import reduce

product=lambda X,Y:X*Y

def main():
    a=int(input("Enter number : "))
    b=[]
    for i in range(a):
        no=int(input())
        b.append(no)
    
    ans1=reduce(product,b)
    print("Product : ",ans1)
      
if __name__=="__main__":
    main()