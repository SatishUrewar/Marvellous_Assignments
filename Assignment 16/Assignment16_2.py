#2. Write a program to read and display the contents of a file data.txt.

def main():

    try:
        file = open("data.txt", 'r')
        print(file.read())
    except FileNotFoundError:
        print("Error data.txt not found")

if __name__ == "__main__":
    main()
