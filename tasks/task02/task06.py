from sys import stdout


def newPrint(object, lineBreak='\n'):
    return stdout.write(str(object)+lineBreak)


newPrint(4)
newPrint('qaz')
