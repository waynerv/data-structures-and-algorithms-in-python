""" 基于 list 的字典实现
"""

from assoc import Assoc


class DictList:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def num(self):
        return len(self._elems)

    def search(self, key):
        for a in self._elems:
            if a.key == key:
                return a.value
        return None

    def insert(self, key, value):
        self._elems.append(Assoc(key, value))

    def delete(self, key):
        for i in range(len(self._elems)):
            if self._elems[i].key == key:
                self._elems.pop(i)
                return

    def entries(self):
        for a in self._elems:
            yield a.key, a.value

    def values(self):
        for a in self._elems:
            yield a.value
# end of class

class DictOrdList(DictList):
    def insert(self, key, value):
        elems = self._elems
        low, high = 0, len(elems)-1
        while low <= high:  # There are elements in the interval
            mid = (low + high) // 2
            if key == elems[mid].key:
                elems[mid].value = value
            if key < elems[mid].key:
                high = mid - 1  # continue in the lower half part
            else:
                low = mid + 1   # continue in the higher half part

    def search(self, key):
        elems = self._elems
        low, high = 0, len(elems)-1
        while low <= high:  # There are elements in the interval
            mid = (low + high) // 2
            if key == elems[mid].key:
                return elems[mid].value
            if key < elems[mid].key:
                high = mid - 1  # continue in the lower half part
            else:
                low = mid + 1   # continue in the higher half part

if __name__ != "main":
    from random import randint

    dic1 = DictList()

    for i in range(10):
        dic1.insert(randint(1, 50), randint(1, 100))

    for k, v in dic1.entries():
        print(k, v)

    print("-"*30)

    for i in range(20):
        key = randint(1, 50)
        r = dic1.search(key)
        if r:
            print(key, r)
        dic1.delete(key)

    print("-"*30)
    for e in dic1.entries():
        print(e)
