from random import randint

n = randint(1,100)

cont=True

while cont:
    guess=int(input('Guess a number'))
    if guess>n:
        print('too high')
    elif guess<n:
        print('too low')
    else:
        print('amazing!')
        cont=False