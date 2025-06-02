#Sum of First N Natural Numbers
#Write a recursive function to calculate sum from 1 to n.sum_n(5)→15

sum=0

def Addition(no):
    global sum
    if(no >= 1):
        sum=sum+no
        no = no - 1
        Addition(no)
    return sum
    

def main():
    a=int(input("Enter number : "))
    ret=Addition(a)
    print("Sum of First N Natural Numbers is = ",ret)

if __name__ == "__main__":
    main()