from math import log2


def main(b, n, z):
    res = 0
    for j in range(1, n+1):
        for k in range(1, b+1):
            res += log2(56-z**2-51*z)**4-(34*j+k**2)**3
    return res


print(main(2, 7, 0.53))
print(main(5, 2, 0.72))
