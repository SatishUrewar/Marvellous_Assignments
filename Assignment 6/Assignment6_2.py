#Print Sum of Even numbers Between 1 to 100.
#Use a loop to find and print the sum of all even numbers from 1 to 100.

def main():
    a=0
    for i in range(1,101,1):
        if i%2==0:
            a=a+i
    print("Sum of even numbers between 1 to 100 is : ",a)

if __name__=="__main__":
    main()