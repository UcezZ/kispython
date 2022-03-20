from random import random


def sprite():
    s = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(3):
        for j in range(5):
            s[j][i] = s[j][4-i] = True if random() > 0.5 else False
    return s


def printSprite(sprite):
    for i in range(5):
        for j in range(5):
            print('x' if sprite[i][j] else ' ', end='')
        print()


for i in range(10):
    printSprite(sprite())
    print()
