#Write a function that accepts a string and checks whether it is a palindrome.
 
def palindrome(v1):
    
    bb=[]
    for i in range(len(v1)-1,-1,-1):
        bb.append(v1[i])
     
    if(v1==bb):
        print("it is palindrome")
    else:
        print("it is not palindrome")  


def main():
    a=input("Enter string : ")
    b=[]
    for i in range(len(a)):
        b.append(a[i])
    palindrome(b)
        
if __name__=="__main__":
    main()