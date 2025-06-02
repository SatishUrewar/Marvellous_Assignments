#write a program which contains one lambda function which accepts one parameter and return power of two.

power = lambda X: 2**X

def main():
    a = int(input())
    print(power(a))

if __name__=="__main__":
    main()