#Even or odd number Check
#Write a program to check whether the entered number is even or odd.

def main():
    a=int(input("Enter a number : "))
    if a%2==0:
        print(a,"is an Even number.")
    else:
        print(a,"is an Odd Number.")


if __name__=="__main__":
    main()