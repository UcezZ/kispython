from xmlrpc.client import boolean


def rowEquals(row1, row2):
    if len(row1) != len(row2):
        return False
    f = True
    for i in range(len(row1)):
        f &= row1[i] == row2[i]
    return f


def floatConvertCrutch(item):
    cnt = 3-len(item[item.find('.')+1:])
    for i in range(cnt):
        item += '0'
    return item


def transpose(table):
    t = []
    for i in range(len(table[0])):
        t.append([])
    for i in range(len(table)):
        for j in range(len(table[i])):
            t[j].append(table[i][j])
    return t


def main(data):
    for i in range(len(data)-1):
        if (rowEquals(data[i], data[i+1])):
            data.remove(data[i])
    for i in range(len(data)):
        data[i][0] = floatConvertCrutch(data[i][0])
        data[i][1] = 'Выполнено' if data[i][1].lower(
        ) == 'true' else 'Не выполнено'
        data[i][2] = data[i][2].split('.')
        data[i][2].reverse()
        data[i][2] = '.'.join(data[i][2])
        data[i][3] = data[i][3][data[i][3].find('[at]')+4:]
    return transpose(data)


print(main([['0.8', 'false', '2002.11.27', 'kuvasak72[at]mail.ru'], ['0.8', 'false', '2001.03.17', 'zanko70[at]mail.ru'], ['0.5', 'false', '2003.08.12',
      'fazasic64[at]yahoo.com'], ['0.1', 'true', '2001.11.03', 'nozifskij76[at]yahoo.com'], ['0.1', 'true', '2001.11.03', 'nozifskij76[at]yahoo.com']]))
