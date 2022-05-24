def bitcount(i):
    c = 0
    while i > 0:
        if i % 2 == 1:
            c += 1
        i >>= 1
    return c


print(bitcount(127))
print(bitcount(63))
print(bitcount(134))
