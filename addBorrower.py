#adding a new borrower to the list
def addBorrower():
    #get input as id number
    idn = input("Enter the id: ")
    #checking if it exists
    if not searchID(idn):
        #if not, get the other information
        name = input("Enter borrower name: ")
        contact = input("Enter contact e-mail:")
        #oppen the borrowers file in append mode
        with open("borrowers.txt","a") as file:
            #create a string with the new borrower information
            x = f'{idn}, {name}, {contact}\n'
            #write it in the end of the file and close the file
            file.write(x)
        print('Done! The new borrower has been added')
    else:
        print("user already exist")
