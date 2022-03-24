class custom:
    asd = 1
    mnbv = 'lasd'
    qwert = [1, 2, 3]

    def f():
        print('oaoaoammm')
    pass


def EnumerateClassProperties(cls):
    for item in dir(cls):
        if not callable(getattr(cls, item)) and not (item.startswith('__') and item.endswith('__')):
            print(item)


def CallClassMethod(cls, methodName):
    for item in dir(cls):
        if callable(getattr(cls, item)) and item == methodName and not (item.startswith('__') and item.endswith('__')):
            getattr(cls, item)()


EnumerateClassProperties(custom)
CallClassMethod(custom, 'f')
