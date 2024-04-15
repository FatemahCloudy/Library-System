def main():
    system = True
    print('Welcome to the library system!')
    print('Please chose a number from the list: ')
    while system:
        functions()
        print()
        choice = input("Enter the number or ENTER to exit: ")
        if choice == '1':
            lis = bookList()
            print("%-20s %-45s %-20s %-10s %-10s\n"%("ISBN","Title","Author","Year","Status") + '-'*120)
            for i in lis:
                print("%-20s %-45s %-20s %-10s %-10s"%(i[0],i[1],i[2],i[3],i[4]))
            print("-"*120)
            print()
        elif choice == '2':
            lis = borrowerList()
            print("%-7s %-15s %-30s\n"%("ID","Name","Contact")+ '-'*50)
            for i in lis:
                print("%-7s %-15s %-30s"%(i[0],i[1],i[2]))
            print("-"*50)
            print()
        elif choice == '3':
            idn = input("Enter the id: ")
            x = searchID(idn)
            if x:
                print(x)
            else:
                print("ID not found")
            print()
        elif choice == '4':
            isbn = input("Enter the ISBN: ")
            x = searchISBN(isbn)
            if x:
                print(x)
            else:
                print("ISBN not found")
            print()
        elif choice == '5':
            addBorrower()
            print()
        elif choice == '6':
            newBooks()
            print()
        elif choice == '7':
            deleteBook()
            print()
        elif choice == '8':
            addBook()
            print()
        elif choice == '9':
            checkout()
            print()
        elif choice == '10':
            returning()
            print()
        elif choice == '11':
            userCheckouts()
            print()
        elif choice == '':
            exit_system()
            system = False
        else:
            print('Wrong input')
            print()
main()
