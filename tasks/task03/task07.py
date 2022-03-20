from matplotlib import pyplot as p, colors as c
from numpy import random as r


def sprite():
    s = r.randint(0, 2, 25).reshape(5, 5)
    for i in range(3):
        for j in range(5):
            s[j][i] = s[j][4-i]
    return s


def printSprite(sprite):
    for i in range(5):
        for j in range(5):
            print(sprite[i][j], end=' ')
        print()


s = sprite()
printSprite(s)
f, a = p.subplots()

a.imshow(s, cmap=c.ListedColormap(['white', 'black']))

p.show()
