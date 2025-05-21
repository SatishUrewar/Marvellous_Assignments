#Area and Perimeter or Rectangle
#Accept the length and width of a rectangle.
#Calculate and display the area and perimeter.

def main():
    l=int(input("Enter Length : "))
    w=int(input("Enter width : "))

    A=l*w
    P=2*(l+w)

    print("Area : ",A)
    print("Perimeter : ",P)

if __name__=="__main__":
    main()