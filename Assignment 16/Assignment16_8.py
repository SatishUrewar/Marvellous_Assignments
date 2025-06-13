#8. Write a script to remove all blank lines from a file.
#Save the cleaned output to a new file.


def main():
    file1 = input("Enter input file name:  ")
    file2 = input("Enter output file name: ")

    f1 = open(file1, "r")
    f2 = open(file2, "w")

    for line in f1:
        if line.strip():
            f2.write(line)

if __name__ == "__main__":
    main()
