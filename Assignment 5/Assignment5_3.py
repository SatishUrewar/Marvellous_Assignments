#Voting Eligibility Checker
#Accept age from the user and check whether the person is eligible to vote.
#(Age should be 18 or above.)

def main():
    a=int(input("Enter age : "))
    if a>=18:
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")

if __name__=="__main__":
    main()