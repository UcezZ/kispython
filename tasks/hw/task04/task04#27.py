from math import cos


def main(n):
    if n == 0:
        return -0.20
    else:
        return cos(6*main(n-1)**3+91*main(n-1)**2)**3


print(main(3))
print(main(4))
