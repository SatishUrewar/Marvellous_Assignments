#3. Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. 
#Accept file name through command line arguments.

import sys

def main():
    existingFile = sys.argv[1]
    f1 = open(existingFile,'r')
    f2 = open("demo.txt",'w')
    f2.write(f1.read())

if __name__=="__main__":
    main()
