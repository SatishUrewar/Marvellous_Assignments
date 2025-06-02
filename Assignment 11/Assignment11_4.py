#Power Function Using Recursion
#Write a recursive function to calculate x^n.power (2, 3)→8 

def power(v1,v2):
    if (v2==0):
     return 1
    v3=power(v1,v2-1) 
    result=v1*v3  
    return result
def main():
    a=int(input("Enter number : "))
    b=int(input("Enter power : "))
    ret=power(a,b)
    print(ret)
    

if __name__ == "__main__":
    main()