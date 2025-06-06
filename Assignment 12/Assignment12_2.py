class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        self.Radius=float(input("Enter radius : "))
        return self.Radius
        
    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius
        return self.Circumference

    def Display(self):
        
        print("Radius is : ",self.Radius)
        print("Area is : ",self.Area)
        print("cicumference of circle is: ",self.Circumference)

def main():
    obj1=Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

if __name__=="__main__":
    main()