import math


def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


def naming(name):
    print(f'hello, {name}')
    naming2(name)
    print(f'well, i think gg')
    bye()


def naming2(name):
    print(f'how are you {name}')


def bye():
    print(f'bb')


def recurs(a):
    if a == 1:
        return 1
    else:
        return a * recurs(a - 1)


print(countdown(5))
print(naming('vanya'))
print(recurs(11))
print(math.factorial(11))