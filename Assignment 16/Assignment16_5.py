#5. Write a program to read a file line by line and display only those lines that contain more than 5 words.

def main():
    filename = input("Enter the file name: ")
    file = open(filename, 'r')

    for line in file:
        words = line.split()
        if len(words) > 5:
            print(line)

if __name__ == "__main__":
    main()
