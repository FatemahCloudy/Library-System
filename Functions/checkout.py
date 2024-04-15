def checkout():
    userID  = input('Enter ID number: ')
    with open('borrowers.txt') as borrowers:
        exist = False
        for line in borrowers:
            if userID in line:
                exist = True
        if not exist:
            addBorrower()
#gitting the input as ISPN
    isbn = input("Enter the ISBN: ")
    #checking if it exists
    book = searchISBN(isbn)
    #in case it doesn't
    if not book:
        print('This book does not exist')
        return False
    elif book[4] == 'Unavailable':
        print('This book is not available')
        return False
    #in case it exists
    else:
        updateStatus(isbn, 'Unavailable')
        # Then, record the chckout in the checkouts file
        from datetime import datetime, timedelta
        today = datetime.now().date()
        returning_date = today + timedelta(days = 30)
        with open('checkouts.txt', 'a') as checkouts:
            data = f'\n{isbn},{userID},{today},{returning_date}'
            checkouts.writelines(data)
        print(f'{book[1]} is checked out successfully. Enjoy reading!')
