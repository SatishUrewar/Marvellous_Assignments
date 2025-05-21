#Celsius to Fahrenheit Converter
#Accept temperature in celsius and convert it to Fahrenheit using the formula:
#F = (C*9/5)+32


def main():
    C=float(input("Enter temperature in Celsius : "))
    F = (C * 9/5) + 32
    print("Temperature in Fahrenheit : ",F)

if __name__=="__main__":
    main()