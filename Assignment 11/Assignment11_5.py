#Count Zeros in a Number (Recursively)
#Write a recursive function to count how many zeros are in the given number.count_zeros(1020300) 4

def CntZero(no,n1):    
    if (n1==len(no)):
     return 0
    count=0
    crntnum=no[n1]
    rcount=CntZero(no,n1+1)
    if (crntnum==0):
     count=1
    return count+rcount

def main():
    a=[]
    b=input("Enter number : ")
    for i in range(len(b)):
     a.append(int(b[i]))

    ret=CntZero(a,0)
    print(ret)
    

if __name__ == "__main__":
    main()