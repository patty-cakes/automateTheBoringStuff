def collatz(collIn):
    collOut = int()
    while collOut != 1:
        if collIn % 2 == 0: # catches even numbers
            collOut = collIn // 2
            print(str(collOut))
            collIn = collOut
        elif collIn % 2 == 1: # catches odd numbers
            collOut = collIn * 3 + 1
            print(str(collOut))
            collIn = collOut

print('Enter a number:')

try:
    collatz(int(input()))
except ValueError:
        print('Error: invalid argument.')
