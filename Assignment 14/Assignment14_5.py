class BankAccount:

    def __init__(self):
        self.Name=""
        self.Balance=0 
        self.Accountnumber=0   

    def Deposit(self):
        self.Name=input("enter name : ")
        self.Accountnumber=int(input("Enter account number : "))
        self.Balance=float(input("Enter amount  : "))
    
    def Withdraw(self):

        w=float(input("Enter amount to be withdrawn : "))
        if (w<=self.Balance):
            return self.Balance-w
        else:
            print("Insufficient funds")

    def Display(self):
        print("Name : "+self.Name)
        print("Ammount : ",self.Balance)
        print("Account Number: ",self.Accountnumber)

def main():
    obj1=BankAccount()
    obj1.Deposit()
    obj1.Display()
    ret=obj1.Withdraw()
    print("amount remaing after withdrwarn : ",ret)

if __name__=="__main__":
    main()