def fast_mul(x, y):
    r = 0
    c = 0
    while (y > 0):
        if (y % 2 == 1):
            r += x << c
        c += 1
        y >>= 1
    return r


print(fast_mul(16, 5))
