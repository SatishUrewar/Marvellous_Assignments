#Accept a list of integers from the user and use the map() function to double each value.

double = lambda x: x*2

def main():
    a=int(input("Enter Number: "))
    b=[]
    for i in range(a):
        no=int(input())
        b.append(no)

    ans1=list(map(double,b))
    print("Double List: ",ans1)

if __name__=="__main__":
    main()
    