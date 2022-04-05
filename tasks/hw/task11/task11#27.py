from struct import unpack


def readA(bin, offset):
    data = dict()
    data['A1'] = []
    for i in range(3):
        t, o = readB(bin, offset)
        offset = o
        data['A1'].append(t)
    data['A2'] = unpack('f', bin[offset:offset+4])[0]
    offset += 4
    t, o = readD(bin, offset)
    data['A3'] = t
    offset = o
    data['A4'] = unpack('h', bin[offset:offset+2])[0]
    offset += 2
    t = unpack('I', bin[offset:offset+4])[0]
    offset += 4
    o = unpack('h', bin[offset:offset+2])[0]
    offset += 2
    data['A5'] = unpack(str(t)+'s', bin[o:o+t])[0].decode()
    data['A6'] = readE(bin, unpack('I', bin[offset:offset+4])[0])
    offset += 4
    data['A7'] = list(unpack('7b', bin[offset:offset+7]))
    offset += 7
    data['A8'] = unpack('B', bin[offset:offset+1])[0]
    return data


def readB(bin, offset):
    data = dict()
    data['B1'] = unpack('B', bin[offset:offset+1])[0]
    offset += 1
    t, o = readC(bin, offset)
    data['B2'] = t
    return data, o


def readC(bin, offset):
    data = dict()
    data['C1'] = unpack('B', bin[offset:offset+1])[0]
    offset += 1
    data['C2'] = unpack('B', bin[offset:offset+1])[0]
    offset += 1
    return data, offset


def readD(bin, offset):
    data = dict()
    data['D1'] = unpack('h', bin[offset:offset+2])[0]
    offset += 2
    data['D2'] = unpack('Q', bin[offset:offset+8])[0]
    offset += 8
    return data, offset


def readE(bin, offset):
    data = dict()
    data['E1'] = unpack('I', bin[offset:offset+4])[0]
    offset += 4
    t = unpack('I', bin[offset:offset+4])[0]
    offset += 4
    o = unpack('H', bin[offset:offset+2])[0]
    offset += 2
    data['E2'] = unpack(str(t)+'d', bin[o:o+8*t])
    data['E3'] = unpack('I', bin[offset:offset+4])[0]
    return data


def main(data):
    return readA(data, 4)


print(main(b'HWHR(D\r\xc0\x0bz\xad\x1c\xbc\xae\x90\xd8\xbe\xe9(\x94AH\xb5v\x0c!\xc9Q'
           b'\xd6\x05\x00\x00\x00/\x00D\x00\x00\x00\xa9J\xd4\x9c\xb9\xaa\xe6\xa8ulkzb'
           b'\x80S\xea_\xecs\x9f?\xbc\xee\x17\xaa^\xc1\xdf?\x0c\x9d\x7fS\x02\x00\x00\x00'
           b'4\x00\xfaz\xbc\x1f'))
