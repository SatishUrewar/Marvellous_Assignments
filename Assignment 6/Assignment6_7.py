#Accept 5 number from user.
#Find and print the largest number.

def main():
    print("Enter 5 numbers: ")

    num1=int(input())
    num2=int(input())
    num3=int(input())
    num4=int(input())
    num5=int(input())

    largest = num1

    if num2>largest:
        largest=num2
    elif num3>largest:
        largest=num3
    elif num4>largest:
        largest=num4
    else:
        largest=num5
    
    print("Maximum number is: ",largest)

if __name__=="__main__":
    main()