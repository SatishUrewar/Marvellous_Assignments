#Write a program which accepts file name from user and check whether that file exists in current directory or not.

import os

def main():
    fileName = input("Enter the file name you want to check:")

    if os.path.isfile(fileName):
        print("The given File name exist in the directory.")
    else:
        print("The given File Name does not exist in the directory")


if __name__=="__main__":
    main()