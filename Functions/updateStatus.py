def updateStatus(isbn, status):
    #checking if it exists
    book = searchISBN(isbn)
    #in case it doesn't
    if not book:
        print('This book does not exist')
        return False
    #in case it exists
    else:
        #getting the book information in a list instead of a tuple
        result = list(book)
        result[4] = status
        new = [book, tuple(result)]
        books = open ('books.txt')
        lines = ""
        # iterating through the lines of the file(each line is a tuple for a book)
        for line in books:
            #adding the line to a string
            lines +=line
        #replacing the old information with the new one
        update = lines.replace(str(new[0]), str(new[1]).strip())
        #opening the file in write mood (clear any data)
        file = open("books.txt", 'w')
        #writing the whole updated text
        file.write(update) 
        #closing both files
        file.close()
        books.close()
