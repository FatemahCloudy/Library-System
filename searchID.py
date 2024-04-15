#finding a borrowers by their ID number
def searchID (idn):
    flag = False
    #getting the list of borrowers
    lis = borrowerList()
    #iterating through each tuple
    for i in lis:
        #checking if the IDs mach
        if i[0] == idn:
            flag =  True
            #returning the borrower informations
            return tuple(i)
    return flag
