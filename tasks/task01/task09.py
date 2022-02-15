def naive_mul(x, y):
    r = 0
    for i in range(0, y):
        r += x
    return r


for i in range(0, 100):
    print(naive_mul(10, i))
