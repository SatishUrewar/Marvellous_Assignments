#5. Accept file name and one string from user and return the frequency of that string from file.

def main():
    fileName = input("Enter file name: ")
    word = input("Enter word to search: ")

    count = 0
    f = open(fileName, 'r')

    for line in f:
        count += line.count(word)

    print("Count:", count)

if __name__ == "__main__":
    main()
