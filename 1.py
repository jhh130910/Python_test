import sys

lines = [] # contains the lines of the file. 
jumps = {}
eax = 0
zeroFlag = False

def main():
    pass


class InvalidSyntax (Exception):
    def __init__ (self):
        pass

class Token():
    def __init__ (self, token, t):
        self.token = token
        self.t = t

def loadFile(fileName):
    """
        loadFile: This function loads the file and reads its lines.
    """
    global lines
    fo = open(fileName)
    for line in fo:
        lines.append(line)
    fo.close()

class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score
# isinstance ...
a = '10'
b = 3
c = [1, 2, 3]
d = (1, 2, 3)
f = Student('Eden', 99.9)
print(isinstance(a,  str))      # True
print(isinstance(b, int))       # True
print(isinstance(c, list))      # True
print(isinstance(d, tuple))     # True
print(isinstance(x, bool))     # True
print(isinstance(f, Student))   # True


def usage():
    pass

def bye():
    pass
