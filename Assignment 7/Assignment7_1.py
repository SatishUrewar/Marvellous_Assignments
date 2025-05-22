#Write two lambda functions:
    # One to calculate square of a number
    # Another to calculate cube of a number


square=lambda x: x*x
cube = lambda x : x*x*x

def main():
    num=int(input("Enter number: "))

    ans1=square(num)
    ans2=cube(num)

    print("Square : ",ans1)
    print("Cube : ",ans2)




if __name__=="__main__":
    main()