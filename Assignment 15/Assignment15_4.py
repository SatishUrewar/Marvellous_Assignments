#4. Write a program which accept two file names from user and compare contents of both the files. 
#If both the files contains same contents then display success otherwise display failure. 
#Accept names of both the files from command line.

import sys

def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if open(file1).read() == open(file2).read():
        print("Success")
    else:
        print("Failure")


if __name__=="__main__":
    main()