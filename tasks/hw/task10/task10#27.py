def countOf(data, row):
    c = 0
    for r in data:
        if r == row:
            c += 1
    return c


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
    i = 0
    while i < len(data):
        if countOf(data, data[i]) > 1:
            data.remove(data[i])
            i = 0
        else:
            i += 1
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

print(main([['0.3', 'true', '2000.05.05', 'sotisak28[at]yahoo.com'], ['0.6', 'true', '2004.03.24', 'lolesidi88[at]gmail.com'], [
      '0.7', 'false', '2003.04.05', 'zifov41[at]yahoo.com'], ['0.6', 'true', '2004.03.24', 'lolesidi88[at]gmail.com']]))
