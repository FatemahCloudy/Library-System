#run first before any other function

def cleaning(file):
    lis = []
    #each line
    for i in file:
        i = i.strip()
        #each word
        for k in i:
            #each char
            for q in k:
                if q in "''()" :
                    i= i.replace(q,"")
        #each item
        i = i.split(",")
        for l in i:
            m = l.strip()
            i[i.index(l)] = m
        j = tuple(i)
        lis.append(j)
    file.close()
    return lis
