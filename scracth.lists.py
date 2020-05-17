def findReplace(target,find,replace):
    if find not in target:
        print(find,' is not in the list.')
    else:
        for i in range(len(target)):
            if target[i] == find:
                target[i] = str(replace)
        print('The list has been amended:')
        print(target)


list = ['dog','cat','bat']

print()
print('This is my list: ' + str(list))

list *= 2
catCount = list.count('cat')
print()
print('This is my list x2: ' + str(list))

print()
print('There are ' + str(catCount) + ' instances of cat in the list.')

print()
print('Time to append a moo at the end:')
list.append('moo')
print(str(list))

print()
print('Now to insert an emu in 3rd spot:')
list.insert(2,'emu')
print(str(list))

print()
print('Type name of animal to remove:')
remove = input()
print()
print('Type name of animal to replace it:')
replace = input()

findReplace(list,remove,replace)

#def findandreplace(list,find,replace)
#    if removeBeast not in list:
#        print()
#        print('There are no beasts by that name in the list!')
#    else:
#        for i in range(len(list)):
#            if list[i] == removeBeast:
#                list[i] = 'frog'
#    print()
#    print()
#    print('The list has been amended:')
#    print()
#    print(list)
