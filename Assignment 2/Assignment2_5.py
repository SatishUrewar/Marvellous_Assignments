def prime(v1):
    if v1 < 2:
        return True
    for i in range(2,v1):
     if (v1 % i==0):
        return  True
     
    return False

    
def main():

    no1=int(input("enter number : "))
    result=prime(no1)
    if (result==True):
       print("not prime")
    else:
       print("prime")
               
if __name__=="__main__":
    main()

    