def sort(n,li):
    for i in range(n):
        for j in range(n-i-1):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
    return(li[0])

def main():
    a=int(input("Enter how many number you want to store : "))
    b=list()
    for i in range(a):
        no=int(input())
        b.append(no)
    result=sort(a,b)
    print("your minimum num is : ",result)
    
#inbuilt function
#b.sort(reverse=True)
    #c=b[0]
    #print(c) 
if __name__=="__main__":
    main()