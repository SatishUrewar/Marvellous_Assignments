#Write a program which accept number from user and return addition of digits in that number.

def main():
    a=input("enter number : ")
    b=list(map(int,a))
    result=0
    for i in b:
        result=result+i

    print("your addition is : ",result)
    
       
   

if __name__=="__main__":
    main()
