#Print Pattern Using Recursion (Right Triangle)
#Write a recursive function to print the following pattern:

#* 
#* * 
#* * *
#* * * *

def Display(no, n1):
    if n1 == no:
        return
    print("*", end=" ")
    Display(no, n1 + 1)

def Display2(no, n1):
    if n1 > no:
        return
    Display(n1, 0)
    print()
    Display2(no, n1 + 1)

def main():
    Display2(4,1)

if __name__ == "__main__":
    main()