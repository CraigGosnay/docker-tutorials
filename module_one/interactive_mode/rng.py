from random import randint

min_n = int(input('Enter min number: '))
max_n = int(input('Enter max number: '))

if max_n < min_n:
    print('invalid input!')
else:
    rnd = randint(min_n, max_n)
    print(rnd)