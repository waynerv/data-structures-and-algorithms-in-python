from collections import deque


class Queue(object):
    def __init__(self):
        self._items = deque()

    def append(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.popleft()

    def empty(self):
        return len(self._items) == 0


class Stack(object):
    def __init__(self):
        self._items = deque()

    def push(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.pop()

    def empty(self):
        return len(self._items) == 0


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class Bintree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """通过节点信息构造二叉树
        第一次遍历使用data数据分别构造 node 节点并存入字典，node.left和node.right仍然为None
        第二次遍历从字典中取出node节点并给 root 和 孩子赋值(用node赋值)
        最后用 root 节点初始化这个类并返回一个对象

        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
            if node_data['is_root']:
                root = node
        return cls(root)

    def preorder_trav(self, node):
        """先序遍历"""
        if node is not None:
            print(node.data)  # 递归函数里先处理根
            self.preorder_trav(node.left)  # 递归处理左子树
            self.preorder_trav(node.right)  # 递归处理右子树

    def inorder_trav(self, node):
        """中序遍历"""
        if node is not None:
            self.preorder_trav(node.left)
            print(node.data)
            self.preorder_trav(node.right)

    def postorder_trav(self, node):
        """后序遍历"""
        if node is not None:
            self.preorder_trav(node.left)
            self.preorder_trav(node.right)
            print(node.data)

    def preorder_trav_use_stack(self, node):
        s = Stack()
        while node or s.empty() is not None:
            while node:
                print(node.data)
                s.push(node)
                node = node.left
            if s.empty() is not None:
                node = s.pop()
                node = node.right



    def layer_trav_use_queue(self, node):
        """使用队列进行层序遍历"""
        q = Queue()
        q.append(node)
        while not q.empty():
            curnode = q.pop()
            print(curnode.data)
            if curnode.left:
                q.append(curnode.left)
            if curnode.right:
                q.append(curnode.right)

    def layer_trav_use_list(self, node):
        """
        使用两个列表进行层序遍历，一个列表存放当前层节点，一个列表存放下一层节点
        :param node:
        :return:
        """
        curnodes = [node]
        next_nodes = []
        while curnodes or next_nodes:
            for item in curnodes:
                print(item.data)
                if item.left:
                    next_nodes.append(item.left)
                if item.right:
                    next_nodes.append(item.right)
            curnodes = next_nodes
            next_nodes = []

    def reverse(self, node):
        """
        和遍历操作类似，递归进行交换
        :param node:
        :return:
        """
        if node is not None:
            node.left, node.right = node.right, node.left
            self.reverse(node.left)
            self.reverse(node.right)


btree = Bintree.build_from(node_list)
btree.preorder_trav(btree.root)
