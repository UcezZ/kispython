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
    t = unpack('L', bin[offset:offset+4])[0]
    offset += 4
    o = unpack('h', bin[offset:offset+2])[0]
    offset += 2
    data['A5'] = unpack(str(t)+'s', bin[o:o+t])[0].decode()
    data['A6'] = readE(bin, unpack('L', bin[offset:offset+4])[0])
    offset += 4
    data['A7'] = unpack('7b', bin[offset:offset+7])
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
    data['E1'] = unpack('L', bin[offset:offset+4])[0]
    offset += 4
    l = unpack('L', bin[offset:offset+4])[0]
    offset += 4
    o = unpack('H', bin[offset:offset+2])[0]
    offset += 2
    data['E2'] = unpack(str(l)+'d', bin[o:o+8*l])
    data['E3'] = unpack('L', bin[offset:offset+4])[0]
    return data


def main(data):
    readA(data, 4)


print(main(b'HWHR(D\r\xc0\x0bz\xad\x1c\xbc\xae\x90\xd8\xbe\xe9(\x94AH\xb5v\x0c!\xc9Q'
           b'\xd6\x05\x00\x00\x00/\x00D\x00\x00\x00\xa9J\xd4\x9c\xb9\xaa\xe6\xa8ulkzb'
           b'\x80S\xea_\xecs\x9f?\xbc\xee\x17\xaa^\xc1\xdf?\x0c\x9d\x7fS\x02\x00\x00\x00'
           b'4\x00\xfaz\xbc\x1f'))
print(main(b'HWHR\rJ/X\xe5\xf1\xd76f\x97\x1e,\xbe\\b\xf6z\xa5y\x03M1\x1c\xbe+\x06\x00\x00'
           b'\x00/\x00M\x00\x00\x00\xf4f\xd9\x9bq#"\x9aedugbz\xe6\x9e\xca;\xa1\x7f\xed'
           b'\xbf$\xea\xa9\xa1\xe2\x96\xea?8\x81C\x1c!\xcf\xed\xbf9\xc1D3\x03\x00\x00'
           b'\x005\x00qt\x83\xd4'))
