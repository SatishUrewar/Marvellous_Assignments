def main():
    a=int(input("enter number : "))
    
    for i in range(a):
        for j in range(1,a+1):
            print(j, end="     ")
        print()
   

if __name__=="__main__":
    main()