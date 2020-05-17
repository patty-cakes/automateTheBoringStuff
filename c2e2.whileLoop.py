attempt=int(1)

while True:
    print('Attempt: ' + str(attempt))
    print('Please type your name: ')
    name = input()
    attempt=attempt+1
    if name == 'your name':
        print()
        print('Finally!')
        break
    if attempt >=4:
        print()
        print('Too many attempts!')
        break
print()
print('GAME OVER')



