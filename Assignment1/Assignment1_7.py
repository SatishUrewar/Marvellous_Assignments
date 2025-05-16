#Write a program which contains one function what accept one number from user and return if number is divisible by 5 otherwise return false.

def ChkNum(num):
    num = num%5==0
    return num

def main():
    print("Enter any number : ")
    num=int(input())
    if ChkNum(num):
        print("True")
    else:
        print("False")


if __name__=="__main__":
    main()