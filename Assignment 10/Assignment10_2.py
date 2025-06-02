#write a program which contains one lambda function which accepts two parameters and return its multiplication.

multi = lambda X,Y: X*Y

def main():
    a = int(input())
    b = int(input())
    print(multi(a,b))

if __name__=="__main__":
    main()