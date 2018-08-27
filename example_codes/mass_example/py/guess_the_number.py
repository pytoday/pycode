#Guess Numbers
import random
secret_number = random.randint(1,30)

print('I\'m thinking of a number between 1 and 30.')

for guess_count in range(1,7):
    print('guess a number:')
    while True:
        try:
            guess_number = int(input())
        except ValueError:
            print('Please input a number')
            continue
        break

    if guess_number < secret_number:
        print('Your guess is  too low.')
    elif guess_number > secret_number:
        print('Your guess is too high.')
    else:
        break    #this condition is the right number
if guess_number == secret_number:
    print('Good job! You guessed my number in' + str(guess_cunt) + 'guess')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))
