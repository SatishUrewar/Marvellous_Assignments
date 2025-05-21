#Find Largest Among three Numbers
#Accept three numbers from the user and print the largest using nested if-else statements.

def main():
    n1=int(input("Enter 1st number: "))
    n2=int(input("Enter 2nd number: "))
    n3=int(input("Enter 3rd number: "))

    if n1>=n2:
        if n2>=n3:
            largest = n1
        else:
            largest = n3
    else:
        if n2>=n3:
            largest = n2
        else:
            largest = n3
    print("Largest number is: ",largest)


if __name__=="__main__":
    main()