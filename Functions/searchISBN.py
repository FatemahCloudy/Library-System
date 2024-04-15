#finding a book by its ISPN

def searchISBN (isbn):
    flag = False
    #getting the list of books
    lis = bookList()
    #iterating through each tuple
    for i in lis:
        #checking if the ISPNs mach
        if i[0] == isbn:
            flag =  True
            #returning the book informations
            return tuple(i)   
    return flag
