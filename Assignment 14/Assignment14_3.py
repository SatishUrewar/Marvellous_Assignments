class Book:
    def __init__(self,A):
        self.price=A

    def get(self):
        print("Price of book is : ",self.price)
    
    def set(self,v1):
        self.price=v1
        print("updated price is : ",self.price)
        

def main():
    a=int(input("Enter price of book : "))
    obj1=Book(a)
    obj1.get()

    b=int(input("set the price of book : "))
    obj1.set(b)
    
if __name__=="__main__":
    main()