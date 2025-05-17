
def main():
    sum=0
    no1=int(input("enter number : "))
    for i in range(1,no1):
        if (no1 % i==0):
            sum=sum+i
    print(sum)
               
if __name__=="__main__":
    main()

    