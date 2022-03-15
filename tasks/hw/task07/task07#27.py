def bitSlice(hex, bitStart, bitEnd):
    mask = 0
    for i in range(bitStart, bitEnd):
        mask |= 1 << i
    return hex & mask


def main(hex):
    # var "t" for only PEP8 standard
    t = bitSlice(hex, 26, 32)
    t |= bitSlice(hex, 0, 10) << 16
    t |= bitSlice(hex, 10, 15) << 1
    t |= bitSlice(hex, 15, 26) >> 15
    return t
