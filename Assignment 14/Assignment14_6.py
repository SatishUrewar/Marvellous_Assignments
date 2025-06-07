class Calculator:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def Addition(self):
         result=self.no1+self.no2
         print("Addition is :",result)

    def Substraction(self):
         result=self.no1-self.no2
         print("Substraction is :",result)

    def Multiplication(self):
         result=self.no1*self.no2
         print("Multiplication is :",result)

    def Division(self):
         result=self.no1/self.no2
         print("Division is :",result)

def main():
     a=int(input("Enter 1st number : "))
     b=int(input("Enter 2nd number : "))
     obj1=Calculator(a,b)
     obj1.Addition()
     obj1.Substraction()
     obj1.Multiplication()
     obj1.Division()
     
     

if __name__=="__main__":
     main()
    