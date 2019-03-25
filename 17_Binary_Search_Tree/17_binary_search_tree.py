class Array(object):
    def __init__(self, size=32):  # 关键属性：分配空间和存储单位（使用列表的单个元素作为一个存储单位）
        self._size = size
        self._items = [None] * size

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


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('stack full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('stack empty')
        self.head -= 1
        value = self.array[self.head % self.maxsize]
        return value

    def is_empty(self):
        return len(self) == 0


NODE_LIST = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False},
]


class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


class BST(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        node_dict = {}
        for node_data in node_list:
            key = node_data['key']
            node_dict[key] = BSTNode(key, value=key)
        for node_data in node_list:
            key = node_data['key']
            node = node_dict[key]
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
            if node_data['is_root']:
                root = node
            cls.size += 1
        return cls(root)

    def _bst_search(self, subtree, key):
        """
        :return: 返回找到的节点或None（没找到）
        """
        if subtree is None:  # 没找到或树的根节点为None
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)  # 递归搜索左子节点
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)  # 递归搜索右子节点
        else:
            return subtree

    def __contains__(self, key):
        return self._bst_search(self.root, key) is not None

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)  # 所有查找均从根节点开始
        if node is None:
            return default
        else:
            return node.value

    def _bst_min_node(self, subtree):
        if subtree is None:  # 当根节点为None时，返回None
            return None
        elif subtree.left is None:  # 当节点的左子节点为None时，返回当前节点
            return subtree
        else:
            return self._bst_min_node(subtree.left)  # 否则递归的对左子节点调用本函数

    def bst_min(self):  # 返回最小节点的value
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def _bst_max_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._bst_max_node(subtree.right)

    def bst_max(self):
        node = self._bst_max_node(self.root)
        return node.value if node else None

    def _bst_insert_recursive(self, subtree, key, value):
        """插入并且返回根节点
        1. 如果插入位置为空（初始为根节点），构造节点并插入到此位置， 返回此节点（根节点）
        2. 若不为空，则与插入位置节点的key进行比较，若小于，则以此节点的左子节点node.left作为新的插入位置
        3. 在新的插入位置递归的执行1-2步操作，并返回插入的节点（即以该位置为根的子树的根节点）
        """
        if subtree is None:
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert_recursive(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert_recursive(subtree.right, key, value)
        return subtree

    def _bst_insert(self, key, value):
        node = self.root
        if node is None:
            self.root = BSTNode(key, value)
            return
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = BSTNode(key, value)
                    return
                node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = BSTNode(key, node)
                    return
                node = node.right
            # 在add方法中执行以下操作
            # else:
            #     node.key = key
            #     return

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self.root = self._bst_insert_recursive(self.root, key, value)
            self.size += 1
            return True

    def values(self):
        """
        中序遍历二叉树的所有节点，并返回节点的value值
        :return:
        """
        node = self.root
        s = Stack
        while node is not None and not s.is_empty():
            while node is not None:
                s.push(node)
                node = node.left
            if not s.is_empty():
                node = s.pop()
                yield node.value
                node = node.right

    def _bst_remove(self, subtree, key):
        """删除指定节点，返回根节点

        """
        if subtree is None:  # 若树的根节点为None，返回None
            return None
        elif key < subtree.key:  # 从当前节点的左子节点开始递归地执行删除操作
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:  # 从当前节点的右子节点开始递归地执行删除操作
            subtree.right = self._bst_remove(subtree.right, key)
            return subtree
        else:  # 找到了要删除的节点
            if subtree.left is None and subtree.right is None:  # 没有子节点直接删除（父节点指向返回的None）
                return None
            elif subtree.left is None or subtree.right is None:  # 有一个子节点，将父节点指向返回的该子节点
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:  # 有两个子节点，找到后继结点并替换当前节点的key和value，然后在右子树中删除后继结点
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(subtree.right, successor_node.key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)


def test_bst_tree():
    bst = BST.build_from(NODE_LIST)
    for node_dict in NODE_LIST:
        key = node_dict['key']
        assert bst.get(key) == key
    assert bst.size == len(NODE_LIST)
    assert bst.get(-1) is None

    assert bst.bst_min() == 1

    bst.add(0, 0)
    assert bst.bst_min() == 0

    bst.remove(12)
    assert bst.get(12) is None

    bst.remove(37)
    assert bst.get(37) is None

    bst.remove(100)
    assert bst.get(100) is None
