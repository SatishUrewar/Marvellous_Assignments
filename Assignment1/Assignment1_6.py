#Write a program which accept number from user and check whether that number is positive or negative or zero

def main():
    print("Enter any Number : ")
    num=int(input())

    if num>0:
        print("THe given number is positive : ")
    elif num == 0:
        print("The given number is Zero")
    else:
        print("the given number is negative")



if __name__=="__main__":
    main()