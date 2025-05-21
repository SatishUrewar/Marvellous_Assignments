#Vowel or Consonant Check
#Accept a single character from the user and check if it is a vowel (a, e, i, o, u).
#If not print it's a consonant.

def main():
    c=input("Enter any single character : ")
    if c in ('a','e','i','o','u'):
        print(c,"is a vowel")
    else:
        print(c,"is a Consonant")

if __name__=="__main__":
    main()