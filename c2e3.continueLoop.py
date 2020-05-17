attempt=int(1)

while True:
    print('Attempt: ' + str(attempt))
    print('Please type your name: ')
    name = input()
    attempt=attempt+1
    if name != 'Patty':
        continue
    print('Hey Patty - please enter the password')
    password=input()
    if password == 'swordfish':
        break
print()
print('ACCESS GRANTED')



