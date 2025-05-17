#Write a program which accept one number and display below pattern.
#  1
#  1    2
#  1    2    3
#  1    2    3    4
#  1    2    3    4    5
def main():
    a=int(input("enter number : "))
       
    for i in range(a+1):
         for j in range(1,i+1):
             print(j,end="    ")
         print()

if __name__=="__main__":
    main()
