#3. Write a Python script to count the number of lines, words, and characters in a given file.

def main():

    filename = input("Enter the file Name: ")
    file = open(filename,'r')
    data = file.read()

    lines = len(data.splitlines())
    words = len(data.split())
    characters = len(data)

    print("total lines in given file: ",lines)
    print("total words in given file: ",words)
    print("total characters in given file: ",characters)

if __name__=="__main__":
    main()