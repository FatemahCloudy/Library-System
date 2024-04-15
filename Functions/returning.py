def returning():
#gitting the input as ISPN
    isbn = input("Enter the ISBN: ")
    #checking if it exists
    book = searchISBN(isbn)
    #in case it doesn't
    if not book:
        print('This book does not exist')
        return False
    #in case it exists
    else:
        flag = False
        #getting the list of checkout books
        lis = open('checkouts.txt')
        #iterating through each tuple
        for i in lis:
            i = i.split(',')
            #checking if the ISPNs mach
            if i[0] == isbn:
                #returning the book informations
                checkedBook = tuple(i)
                flag = True
        if not flag:
            print("This book is not checked out")
        else:
            updateStatus(isbn, 'Available')
            k = ""
                # iterating through the lines of the file(each line is a tuple for a book)
            for line in lis:
                #adding the line to a string
                k +=line
            #replacing the book information with the new line by an empty string
            file1 = k.replace(str(checkedBook)+"\n","")
            #opening the file in write mood (clear any data)
            file = open("checkouts.txt", 'r+')
            #writing the whole updated text
            file.write(file1.strip()) 
            #close both files
            file.close()
            lis.close()
            print(f'You returned "{book[1]}" successfully, thanks!')
