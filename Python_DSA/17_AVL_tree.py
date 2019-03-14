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
        return node if node else None

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

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self.root = self._bst_insert_recursive(self.root, key, value)
            self.size += 1
            return True

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


class AVLNode(BSTNode):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, *args, **kwargs):
        super(AVLTree, self).__init__()

    @staticmethod
    def LL(a, b):
        """
        :param a: 最小非平衡子树的根
        :param b: 最小非平衡子树的根的左子节点
        :return:
        """
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def RR(a, b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        c = b.right
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:  # c 本身就是插入节点
            a.bf = b.bf = 0
        elif c.bf == 1:  # 新节点在c的左子树
            a.bf = -1
            b.bf = 0
        else:  # 新节点在c的右子树
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c

    def insert(self, key, value):
        """
        1. 查找新节点的插入位置，并在查找过程中记录遇到的最小不平衡子树的根，插入新节点。
        2. 修改从a的子节点到新节点的路径上各节点的平衡因子。
        3. 检查以a为根的子树是否失衡，失衡时做调整。
        4. 连接好调整后的子树，它可能该作为整棵树的根，或作为a原来的父节点的相应方向的子节点。（左或右节点）
        """
        a = p = self.root  # a记录据插入位置最近的平衡因子非0节点，p为遍历的指针变量
        if a is None:  # 若为空树，直接插入为根节点并返回
            self.root = AVLNode(key, value)
            return

        a_parent = p_parent = None  # 维持 a_parent, p_parent 分别为a, p 的父节点, a,p为根节点时父节点为None
        while p is not None:  # 确定插入位置及最小非平衡树
            if key == p.key:  # key存在，修改value值并结束
                p.value = value
                return
            if p.bf != 0: # 更新a记录的平衡因子非0节点
                a_parent, a = p_parent, p

            p_parent = p # 移动 p 指针
            if key < p.key:
                p = p.left
            else:
                p = p.right

        # p_parent 是插入点的父节点， a_parent,a 记录最小非平衡树
        node = AVLNode(key, value)
        if key < p_parent.key:
            p_parent.left = node  # 作为左子节点插入
        else:
            p_parent.right = node  # 作为右子节点插入

        # 新节点已插入， a是最小不平衡子树，将p的位置重置到a的子节点， d为插入新节点后a的平衡因子的变化值
        if key < a.key:  # 新节点在a的左子树， 平衡因子+1
            p = b = a.left
            d = 1
        else:  # 新节点在a的右子树， 平衡因子-1
            p = b = a.right
            d = -1

        # 修改b到新节点路径上各节点的BF值，b为a的子节点
        while p != node:
            if key < p.key:  # p的左子树增高
                p.bf = 1
                p = p.left
            else:  # p的右子树增高
                p.bf = -1
                p = p.right
        if a.bf == 0:  # a 的原BF为0，不会失衡，直接返回
            a.bf = d
            return
        if a.bf == -d:  # 新节点插入在较低子树里，不会失衡，直接返回
            a.bf = 0
            return

        # 新节点插入在较高子树，失衡，必须调整
        if d == 1:  # 新节点在a的左子树
            if b.bf == 1:
                b = AVLTree.LL(a, b)  # LL调整
            else:
                b = AVLTree.LR(a, b)  # LR调整
        else:  # 新节点在a的右子树
            if b.bf == -1:
                b = AVLTree.RR(a, b)  # RR调整
            else:
                b = AVLTree.RL(a, b)  # RL调整

        # 连接调整好后的子树
        if a_parent is None:  # 原a为树根，修改root节点
            self.root = b
        else:  # a不是根节点，新树接在正确位置
            if a_parent.left == a:
                a_parent.left = b
            else:
                a_parent.right = b
