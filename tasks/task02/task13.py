from os import listdir
from os.path import isdir


def fsToGraphviz(path):
    for i in listdir(path):
        print('    '+path.split('\\').pop()+' -> ' +
              i.replace('.', '_').replace('-', '_')+';')
        if isdir(path+'\\'+i):
            fsToGraphviz(path+'\\'+i)


print('digraph G {')
fsToGraphviz('X:\\Common\\AIDA')
print('}')
