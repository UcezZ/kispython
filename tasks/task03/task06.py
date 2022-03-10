from datetime import datetime
from traceback import extract_stack


def run_with_log(func):
    try:
        func()
    except Exception as e:
        logFile = open(datetime.now().strftime('crash-%Y%m%d-%H%M%S.log'), 'a')
        logFile.write('Exception message list:\n')
        for a in e.args:
            logFile.write('\t'+a+'\n')
        logFile.write('Stacktrace:\n')
        for t in extract_stack():
            logFile.write('\tIn module \''+t.filename +
                          '\' at line #'+str(t.lineno)+'\n')


# print(datetime.now().strftime('crash-%Y%m%d-%H%M%S.log'))
run_with_log(lambda: 0/0)
