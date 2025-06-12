#2. Write a program which accept file name from user and open that file and display the contents of that file on screen.

def main():
    fileName = input("ENter the file name you want to open:")
    file = open(fileName,'r')
    print(file.read())

if __name__=="__main__":
    main()