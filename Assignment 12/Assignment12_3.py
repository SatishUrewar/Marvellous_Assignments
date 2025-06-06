class Arithmetic:

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter 1st number : "))
        self.Value2=int(input("Enter 2nd number : "))

    def Addition(self):
        Result=self.Value1+self.Value2A
        return Result   

    def Substraction(self):
        Result=self.Value1-self.Value2
        return Result    

    def Multiplication(self):
        Result=self.Value1*self.Value2
        return Result     

    def Division(self):
        Result=self.Value1/self.Value2
        return Result    

def main():
    obj1=Arithmetic()
    obj1.Accept()

    ret=obj1.Addition()
    print("Addition is : ",ret)

    ret2=obj1.Substraction()
    print("Substraction is : ",ret2)

    ret3=obj1.Multiplication()
    print("Multilpication is : ",ret3)

    ret4=obj1.Division()
    print("Division is : ",ret4)

if __name__=="__main__":
    main()