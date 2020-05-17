def listAnd(inList):
    #inList.insert(-1,'and')
    output = ''
    for i in range(len(inList)-1):
        output += inList[i] + ', '
    output += 'and ' + inList[len(inList)-1] + '.'
    print(output)

mylist = ['apples','apples','apples', 'bananas', 'tofu', 'cats', 'monkey']
listAnd(mylist)
