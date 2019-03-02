class Array(object):
    def __init__(self, size=32, init=None):  # 加入每个槽位的初始值，还是默认为None
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):  # Called to implement evaluation of self[index]实现下标访问.
        return self._items[index]

    def __setitem__(self, index, value):  # Called to implement assignment to self[index].
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    """定义一个 hash 表 数组的槽
        注意，一个槽有三种状态，看你能否想明白。相比链接法解决冲突，二次探查法删除一个 key 的操作稍微复杂。
        1.从未使用过，值为HashMap.UNUSED（None）。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
        2.使用过但是 remove 了，此时值为 HashMap.EMPTY，该探查点后边的元素仍可能是有key
        3.槽正在使用 Slot 节点
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)  # key-value对以slot对象的形式保存在数组中，slot初始值为HashMap.UNUSED
        self.length = 0

    @property
    def _load_factor(self):
        # 负载因子超过0.8重新分配空间
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        """查找key，返回key在数组中的位置
            若index位置的值为UNUSED，说明槽未使用过，key在数组中不存在
            若为EMPTY或key值，则设法返回key在数组中的位置
        """
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:  # 若值为EMPTY，继续探查点后边的元素
                index = (index * 5 + 1) % _len
                continue  # 跳过当前循环的剩余语句
            elif self._table[index].key == key:  # 若值不为EMPTY，检查slot的key值是否等于key
                return index
            else:  # 有值且不为key，则继续探查点后边的元素
                index = (index * 5 + 1) % _len
        return None

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def _slot_can_insert(self, index):
        return self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED

    def __contains__(self, key):  # 实现散列表的 in 操作
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        """向散列表中添加key-value对
        首先查找key是否已经在散列表中，若已存在，重置其value并返回False；
        若不存在，查找可供插入的槽并插入Slot，并检查负载因子，若有必要则进行重哈希
        """
        index = self._find_key(key)
        if index is not None:  # 更新已存在的key
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)  # 用key-value对构造Slot并插入到数组
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        oldtable = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)  # 使用新的大小构造数组
        self.length = 0

        for slot in oldtable:  # 迭代旧表并将非空节点添加到新数组
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:  # 首先检查key是否存在
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:  # 首先检查key是否存在
            raise KeyError()
        else:
            value = self._table[index].value
            self.length -= 1
            self._table[index] = HashTable.EMPTY
            return value

    def __iter__(self):
        """迭代数组中的slot，若slot不为空，则返回其key值
        :return:
        """
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key


class DictADT(HashTable):

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    ll = list(range(30))
    random.shuffle(ll)
    for i in ll:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(ll)
    assert sorted(list(d)) == sorted(ll)