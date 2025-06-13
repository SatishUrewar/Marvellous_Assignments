#6. Write a Python program to copy the contents of one file (source.txt) into another file (destination.txt).

def main():
    source = input("Enter the source file: ")
    destination = input("Enter the destination file: ")

    s = open(source,'r')
    data = s.read()

    d = open(destination,'w')
    d.write(data)

    print("File copied into another file")

if __name__=="__main__":
    main()