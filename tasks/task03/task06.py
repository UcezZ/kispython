from datetime import datetime
from traceback import extract_stack
from os import chdir, path


def run_with_log(func):
    try:
        func()
    except Exception as e:
        chdir(path.dirname(path.abspath(__file__)))
        logFile = open(datetime.now().strftime('trace-%Y%m%d-%H%M%S.log'), 'a')
        logFile.write('Exception message list:\n')
        for a in e.args:
            logFile.write('\t'+a+'\n')
        logFile.write('Stacktrace:\n')
        for t in extract_stack():
            logFile.write('\tIn module \''+t.filename +
                          '\' at line #'+str(t.lineno)+'\n')
        logFile.close()


run_with_log(lambda: 0/0)
