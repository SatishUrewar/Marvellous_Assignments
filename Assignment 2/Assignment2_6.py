#Write a program which accept one number and display below pattern.
# *    *    *    *    *
# *    *    *    *
# *    *    *
# *    *
# * 
def main():
    a=int(input("enter number : "))
    for i in range(a,0,-1):
        print("*\t"*i)

if __name__=="__main__":
    main()
