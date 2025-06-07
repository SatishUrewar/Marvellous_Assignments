class Person:
    def __init__(self,A,B):
        self.name=A
        self.age=B

    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)

    
class Teacher(Person):
    def __init__(self, A, B,C,D):
        super().__init__(A, B)
        self.subject=C
        self.salary=D

    def display(self):
        super().display()
        print("Subject  : ",self.subject)
        print("Salary : ",self.salary)


def main():
    obj1=Teacher("raj",22,"Math",22000)
    obj1.display()

if __name__=="__main__":
    main()