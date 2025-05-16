#Write a program which contains one function named as ChikNum() which accept one parameter as numberr. if number is even then it should display "Even number" otherwise display "odd number" on console.


def ChkNum(value1):
    if(value1%2==0):
        print("The given no is Even :")
    else:
        print("The given no is ODD :")
    

def main():
    print("Enter any number")
    no1=int(input())
    no2=ChkNum(no1)
    
if __name__=="__main__":
    main()


