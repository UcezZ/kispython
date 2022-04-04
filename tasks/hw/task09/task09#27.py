class main:
    state = ''

    def __init__(self):
        self.state = 'A'

    def split(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'F'
            return 4
        if self.state == 'F':
            self.state = 'G'
            return 7
        if self.state == 'G':
            self.state = 'B'
            return 9
        raise KeyError()

    def stash(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6
        if self.state == 'F':
            return 8
        raise KeyError()
    pass


o = main()
print(o.split())  # 0
print(o.split())  # 2
print(o.stash())  # 3
print(o.split())  # KeyError
print(o.stash())  # 5
print(o.stash())  # 6
print(o.stash())  # 8
print(o.split())  # 7
print(o.split())  # 9
print(o.split())  # 2
print(o.split())  # 4
print(o.stash())  # 8'''
'''print(o.split())  # 0
print(o.split())  # 2
print(o.split())  # 4
print(o.stash())  # 8
print(o.stash())  # 8
print(o.split())  # 7
print(o.split())  # 9
print(o.split())  # 2
print(o.stash())  # 3
print(o.stash())  # 5
print(o.stash())  # 6'''
