#Write a program which accept one number and display below pattern.
#  1    2    3    4    5
#  1    2    3    4    5
#  1    2    3    4    5
#  1    2    3    4    5
#  1    2    3    4    5

def main():
    a=int(input("enter number : "))
    
    for i in range(a):
        for j in range(1,a+1):
            print(j, end="     ")
        print()
   

if __name__=="__main__":
    main()
