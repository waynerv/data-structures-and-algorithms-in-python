""" 字典的基本关联类 
"""


class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return "Assoc({0},{1})".format(self.key, self.value)
    
if __name__ == '__main__':
    a1 = Assoc(1, 2)
    print(str(a1))
    pass
