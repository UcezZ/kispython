from math import atan, asin, sin


def main(y):
    if y < 94:
        return atan(72*y**3)+44*asin(y)**3
    elif y < 192:
        return y**6-abs(70*y-y**3)**7
    elif y < 245:
        return y**6
    elif y < 320:
        return sin(y)**6
    else:
        return (34*y+y**2)**6


print(main(108))
print(main(103))
