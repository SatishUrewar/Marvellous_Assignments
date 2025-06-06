class Bookstore:
    NoOfBooks=0
    def __init__(self,A,B):
        self.Name=A
        self.Author=B
        Bookstore.NoOfBooks+=1

    def Display(self):
        print("Name : "+self.Name)
        print("Author : "+self.Author)
        print("No of Books : ",Bookstore.NoOfBooks)

def main():
    obj1=Bookstore("Linux system programmming","Robert love")
    obj1.Display()

    obj2=Bookstore("C Programming ","Dennis Ritchie")
    obj2.Display()


if __name__=="__main__":
    main()
