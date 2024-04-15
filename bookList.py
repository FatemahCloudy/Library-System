#displaying the list of books

def bookList():
    #open the file
    file = open('books.txt')
    #return a list of books as tuples
    return cleaning(file)
