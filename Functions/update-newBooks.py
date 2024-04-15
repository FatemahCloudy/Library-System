#getting the updated information of a book with the original in a list

def update():
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
        #getting the book information in a list instead of a tuple
        result = list(book)
        # asking what item does the user want to change
        editted = int(input("type 1 for name, 2 for auther, 3 for year, or 4 for status: "))
        #change book title
        if editted == 1:
            result[1] = input("Enter updated title: ")
        #change auther name
        elif editted == 2:
            result[2] = input("Enter updated auther: ")
        # change publication year
        elif editted == 3:
            result[3] = (input("Enter updated publication year: "))
        elif editted == 4:
            result[4] = (input("Enter updated status: "))
        #return a list of the old information tuple and the new information tuple
        return [book, tuple(result)]
    
#update the book information in the file
def newBooks():
    #open the books file
    filer = open("books.txt", 'r')
    # calling the function of new information
    new = update()
    #if the book exists
    if new:
        k = ""
        # iterating through the lines of the file(each line is a tuple for a book)
        for line in filer:
            #adding the line to a string
            k +=line
        #replacing the old information with the new one
        file1 = k.replace(str(new[0]), str(new[1]).strip())
        #opening the file in write mood (clear any data)
        file = open("books.txt", 'w')
        #writing the whole updated text
        file.write(file1) 
    #closing both files
    file.close()
    filer.close()
    print('Information has been updated successfully')
