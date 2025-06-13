#1.Write a Python program to create a text file named student.txt and write the names of 5 students into it.

def main():
    file = open("student.txt",'w')

    for i in range(5):
        names = input("Enter the name of sudent: ")
        file.write(names+"\n")
    
if __name__=="__main__":
    main()