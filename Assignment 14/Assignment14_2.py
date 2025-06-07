class Rectangle:
    def __init__(self,A,B):
        self.length=A
        self.width=B

    def Areaperimeter(self):
        Ar=self.length*self.width
        pr=2*(self.length+self.width)
        print("Area : ",Ar,"Perimeter : ",pr)

def main():
    obj1=Rectangle(10,5)
    obj1.Areaperimeter()
    
if __name__=="__main__":
    main()