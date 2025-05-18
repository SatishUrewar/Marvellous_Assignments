#Write a program which contains one lamda function which accepts one parameter and return power of two.

#def power(x):
#   return x**2
power=lambda x : x**2

def main():
    num1 = int(input("Enter any number : "))
    result=power(num1)

    print("Power of given num is : ",result)

if __name__=="__main__":
    main()