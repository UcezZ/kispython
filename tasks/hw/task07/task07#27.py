def main(hex):
    return (hex << 23) >> 7 | (hex >> 26) << 26


print(hex(main(0xfe79050c)))
