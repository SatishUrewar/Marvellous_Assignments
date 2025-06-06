class Numbers:
    def __init__(self,A):
        self.Value=A

    def ChkPrime(self):
        if (self.Value<2):
            return False
        for i in range (2,self.Value):
         if (self.Value%i==0):
            return False
         
    def ChkPerfect(self):
        sum=0
        for i in range(1,self.Value):
          if(self.Value%i==0):
             sum=sum+i
        if(sum==self.Value):
           return True
        
        
    def _Factors(self):
        fact=[]
        for i in range(1,self.Value):
          if(self.Value%i==0):
             fact.append(i)
        return fact
          
    def SumFactors(self):
        sum=0
        fact=self._Factors()
        for i in fact:
           sum=sum+i
        return sum

def main():
    a=int(input("Enter number : "))
    obj1=Numbers(a)
    ret=obj1.ChkPrime()
    if(ret==True):
      print(a," is prime number ")
    else:
      print(a,"is not prime ")

    ret2=obj1.ChkPerfect()
    if(ret2==True):
        print(a," is perfect number ")
    else:
        print(a,"is not perfect number ")

    ret3=obj1._Factors()
    print("Factors are : ",ret3)

    ret4=obj1.SumFactors()
    print("Sum of factors are : ",ret4)

   
if __name__=="__main__":
   main()