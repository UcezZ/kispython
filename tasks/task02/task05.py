import random
db = [
    ['Коллеги,',    'парадигма цифровой экономики',    'открывает новые возможности для',
        'дальнейшего углубления',    'знаний и компетенций.'],
    ['В то же время,',    'контекст цифровой трансформации',    'выдвигает новые требования',
        'бюджетного финансирования',    'непроверенных гипотез.'],
    ['Однако,',    'диджитализация бизнес-процессов',    'несёт в себе риски',
        'синергетического эффекта',    'волатильных активов.'],
    ['Тем не менее,',    'прагматичный подход к цифровым платформам',
        'расширяет горизонты',    'компрометации конфиденциальных',    'опасных экспериментов.'],
    ['Следовательно,',    'совокупность сквозных технологий',    'заставляет искать варианты',
        'универсальной коммодитизации',    'государственно-частных партнёрств.'],
    ['Соответственно,',    'программа прорывных исследований',    'не оставляет шанса для',
        'несанкционированной кастомизации',    'цифровых следов граждан.'],
    ['Вместе с тем,',    'ускорение блокчейн-транзакций',    'повышает вероятность',
        'нормативного регулирования',    'нежелательных последствий.'],
    ['С другой стороны,',    'экспоненциальный рост Big Data',
        'обостряет проблему',    'практического применения',    'внезапных открытий.']
]
for c in range(20):
    if c == 0:
        print(db[0][0], end=' ')
    else:
        for i in range(0, 4):
            print(db[random.randint(0, 7)][i], end=' ')
        print(db[random.randint(0, 7)][4])
