import random

secretNumber = random.randint(1,20) #defines random number

print('I am thinking of a number between 1 & 20; can you guess it?')

for guessTaken in range(1,7):
    print('Take a guess:')
    guess=int(input())

    if guess < secretNumber:
        print('Your guess is too low, try again')
    elif guess > secretNumber:
        print('Your guess is too high, try again')
    else:
        break # guess must be correct, or guess attempt is above 6

if guess == secretNumber:
    print('Good job, you guessed the right number.')
else:
    print('Nope, the number i was thinking of was ' + str(secretNumber) + '.' )
