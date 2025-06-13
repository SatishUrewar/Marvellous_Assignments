#4. Accept 10 numbers from the user and write them into a file named numbers.txt, each on a new line.

def main():
    fileName = input("Enter the file Name: ")
    file = open(fileName,'w')

    for i in range(10):
        b = input("Enter any 10 numbers: ")
        file.write(b+"\n")

if __name__=="__main__":
    main()