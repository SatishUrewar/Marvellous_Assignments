#Accept a list of number and use filter() to keep only even numbers.

even=lambda X:X%2==0

def main():
    a=int(input("Enter number : "))
    b=[]
    for i in range(a):
        no=int(input())
        b.append(no)
    
    ans1=list(filter(even,b))
    print("Even Numbers : ",ans1)
      
if __name__=="__main__":
    main()