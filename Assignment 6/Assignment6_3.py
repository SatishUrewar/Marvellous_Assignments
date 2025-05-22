#Accept a number from the user and print its multiplication table up to 10.

def table(x):
    for i in range(1,11):
        print(x," * ",i,"= ",x*i)


def main():
    num1=int(input("Enter a number : "))
    table(num1)


if __name__=="__main__":
    main()