#displaying the list of borrowers
def borrowerList():
    #opinning the file
    file = open('borrowers.txt')
    #returnung a list of borrowers as tuples
    return cleaning(file)
