#7. Create a file marks.txt with student name and marks. Then read the file and display students who scored more than 75 marks.

def main():
    file = open("marks.txt",'w')

    for i in range(5):
        name = input("Enter student name: ")
        marks = input("Enter the marks: ")
        file.write(name + " " + marks + "\n")

    file = open("marks.txt",'r')

    for line in file:
        name, marks = line.split()
        if int(marks)>75:
            print(name,marks)

if __name__=="__main__":
    main()