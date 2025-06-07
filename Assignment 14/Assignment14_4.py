class student:
    school_name="Saraswati school"
    def __init__(self,A,B):
        self.name=A
        self.roll_no=B


    def Display(self):
        print("Student name : ",self.name)
        print("Student Roll no :",self.roll_no)
        print("School name : ",student.school_name)
        

def main():
    a=input("Enter name of student : ")
    b=int(input("Enter roll no of student : "))
    obj1=student(a,b)
    obj1.Display()
    student.school_name="Balaji high school"
    obj1.Display()

   
    
if __name__=="__main__":
    main()