class BankAccount():
    ROI=10.5

    def __init__(self):
        self.Name=""
        self.Amount=0    

    def Deposit(self):
        self.Name=input("enter name : ")
        self.Amount=float(input("Enter amount : "))
    
    def Withdraw(self):

        w=float(input("Enter amount to be withdrawn : "))
        if (w<=self.Amount):
            return self.Amount-w
        else:
            print("Insufficient funds")

    def CalculateIntrest(self):
        T = float(input("Enter time period in years: "))
        CI=(self.Amount*BankAccount.ROI*T)/100
        return CI

    def Display(self):
        print("Name : "+self.Name)
        print("Ammount : ",self.Amount)

def main():
    obj1=BankAccount()
    obj1.Deposit()
    obj1.Display()
    ret=obj1.Withdraw()
    print("amount remaing after withdrwarn : ",ret)
    ret2=obj1.CalculateIntrest()
    print("Interest is : ",ret2)

if __name__=="__main__":
    main()