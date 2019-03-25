## 目录

  - [01 抽象数据类型和面向对象编程](#01-抽象数据类型和面向对象编程)
  - [02 数组和列表](#02-数组和列表)
    - [array](#array)
    - [list](#list)
    - [用list实现Array ADT](#用list实现array-adt)
  - [03 链表](#03-链表)
    - [单链表](#单链表)
    - [循环双端链表](#循环双端链表)
    - [LRU Cache](#lru-cache)
  - [04 队列](#04-队列)
    - [单链表实现](#单链表实现)
    - [数组实现](#数组实现)
    - [用list实现队列](#用list实现队列)
    - [双端队列 Double ended Queue](#双端队列-double-ended-queue)
  - [05 栈](#05-栈)
    - [使用双端链表实现](#使用双端链表实现)
    - [使用数组实现](#使用数组实现)
  - [06 算法分析](#06-算法分析)
    - [常用时间复杂度](#常用时间复杂度)
    - [常见复杂度增长趋势](#常见复杂度增长趋势)
  - [07 哈希表](#07-哈希表)
    - [冲突及解决策略](#冲突及解决策略)
    - [扩容](#扩容)
    - [使用数组实现ADT](#使用数组实现adt)
  - [08 字典](#08-字典)
    - [Hashable](#hashable)
  - [09 集合](#09-集合)
    - [ADT实现](#adt实现)
    - [python frozenset](#python-frozenset)
    - [BloomFilter布隆过滤器](#bloomfilter布隆过滤器)
  - [10 递归](#10-递归)
    - [用栈模拟递归](#用栈模拟递归)
    - [尾递归](#尾递归)
    - [汉诺塔问题](#汉诺塔问题)
  - [11 线性查找与二分查找](#11-线性查找与二分查找)
    - [线性查找](#线性查找)
    - [二分查找](#二分查找)
    - [求上下界](#求上下界)
  - [12 基本排序算法](#12-基本排序算法)
    - [冒泡排序](#冒泡排序)
    - [选择排序](#选择排序)
    - [插入排序](#插入排序)
    - [希尔排序](#希尔排序)
  - [13 高级排序算法](#13-高级排序算法)
    - [分治法](#分治法)
    - [归并排序](#归并排序)
    - [快速排序](#快速排序)
    - [无序数组寻找第 k 大的数字](#无序数组寻找第-k-大的数字)
    - [排序总结](#排序总结)
  - [14 树与二叉树](#14-树与二叉树)
    - [二叉树的表示](#二叉树的表示)
    - [二叉树的遍历](#二叉树的遍历)
    - [二叉树层序遍历](#二叉树层序遍历)
    - [反转二叉树](#反转二叉树)
  - [15 堆和堆排序](#15-堆和堆排序)
    - [堆的概念](#堆的概念)
    - [堆的操作](#堆的操作)
    - [堆的表示](#堆的表示)
    - [实现一个最大堆](#实现一个最大堆)
    - [实现一个最小堆](#实现一个最小堆)
    - [实现堆排序](#实现堆排序)
    - [Python 里的 heapq 模块](#python-里的-heapq-模块)
    - [Top K 问题](#top-k-问题)
  - [16 优先级队列](#16-优先级队列)
    - [进阶实现](#进阶实现)
  - [17 二叉查找树](#17-二叉查找树)
    - [二叉查找树定义](#二叉查找树定义)
    - [构造一个BST](#构造一个bst)
    - [BST 操作](#bst-操作)
    - [删除节点](#删除节点)
    - [时间复杂度分析](#时间复杂度分析)
    - [平衡二叉树](#平衡二叉树)
    - [B 树与B+ 树](#b-树与b-树)
    - [红黑树](#红黑树)
  - [18 图与图的遍历](#18-图与图的遍历)
    - [有向图的表示](#有向图的表示)
    - [使用邻接表实现图的ADT](#使用邻接表实现图的adt)
    - [图的遍历](#图的遍历)
    - [拓扑排序](#拓扑排序)
    - [最短路径问题与 Dijkstra 算法](#最短路径问题与-dijkstra-算法)
    - [最小生成树问题与 Prim 算法](#最小生成树问题与-prim-算法)
  - [19 Python 常用内置算法和数据结构](#19-python-常用内置算法和数据结构)
  - [20 参考](#20-参考)

## 01 抽象数据类型和面向对象编程

实现抽象数据类型时应注意：

1. 选择哪种数据结构来存储数据？
2. 选中的数据结构是否能支持需要进行的操作？
3. 选用数据结构的效率（时间与空间复杂度）。

## 02 数组和列表

### array

python内置有array类型，但使用限制较多，仅支持同一数据类型的数值、字符串元素，很少使用。

### list

[list的底层C实现](http://python.jobbole.com/82549/)，基于动态数组实现（根据元素数量自动调整大小），CPython实现中， lists 是指向列表对象的指针组成的array数组。各个操作的时间复杂度如下：

| 操作                                  | 平均时间复杂度 |
| ------------------------------------- | -------------- |
| list[index]                           | O(1)           |
| list.append                           | O(1)           |
| list.insert                           | O(n)           |
| list.pop(index), default last element | O(1)           |
| list.remove                           | O(n)           |

### 用list实现Array ADT

用内置的list实现定长数组：

```python
class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item
```

## 03 链表

### 单链表

每个链接表的节点保存一个指向下一个节点的指针

Python中实现指针：将指针指向的对象直接赋值给对象的指针属性（如self.next）。

实现：

```python
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """链接表 ADT
    [ROOT] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        """
        :param maxsize: int or None, 如果是 None，无限扩充
        """
        self.maxsize = maxsize
        self.root = Node()  # 默认 root 节点指向 None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)  # 构造节点
        tailnode = self.tailnode
        if tailnode is None:  # 还没有 append 过，length = 0， 追加到 root 后
            self.root.next = node
        else:  # 否则追加到最后一个节点的后边，并更新最后一个节点是 append 的节点
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        if self.tailnode is None:
            self.tailnode = node

        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        """遍历 从 head 节点到 tail 节点"""
        curnode = self.root.next
        while curnode is not self.tailnode:  # 从第一个节点开始遍历
            yield curnode
            curnode = curnode.next  # 移动到下一个节点
        if curnode is not None:
            yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        """删除包含值的一个节点，将其前一个节点的next指向被查询节点的下一个节点即可

        :param value: 要删除的值
        :return: 1或-1，表明删除操作是否成功
        """
        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:  # NOTE: 注意更新 tailnode
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1  # 表明删除成功
            else:
                prevnode = curnode
        return -1  # 表明删除失败

    def find(self, value):  # O(n)
        """查找一个节点，返回序号，从0开始

        :param value:
        """
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1  # 没找到

    def popleft(self):
        """删除第一个链表节点
        """
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if self.tailnode is headnode:  # 单节点删除 tailnode 的处理
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None
```

时间复杂度：

| 链表操作                      | 平均时间复杂度 |
| ----------------------------- | -------------- |
| linked_list.append(value)     | O(1)           |
| linked_list.appendleft(value) | O(1)           |
| linked_list.find(value)       | O(n)           |
| linked_list.remove(value)     | O(n)           |

### 循环双端链表

特点：

每个节点既保存了指向下一个节点的指针，同时还保存了上一个节点的指针。

可以快速的直接删除节点，在取得节点的情况下直接让其前后节点互指即可实现删除，时间复杂度为 O(1) 。

实现：

```python
class Node(object):
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList(object):
    """循环双端链表 ADT
    循环就是把root的prev指向tail节点，串起来
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:  # 先看看插入的链表是否已满
            raise Exception('LinkedList is full.')
        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is full.')
        node = Node(value=value)

        # if self.root.next is self.root:
        #     self.root.next =node
        #     node.prev = self.root
        #     node.next = self.root
        #     self.root.prev = node
        # else:
        #     headnode = self.headnode()
        #     self.root.next = node
        #     node.prev = self.root
        #     node.next = headnode
        #     headnode.prev = node
        # self.length += 1
        headnode = self.headnode()
        self.root.next = node
        node.prev = self.root
        node.next = headnode
        headnode.prev = node
        self.length += 1

    def remove(self, node):
        """remove
        :param node: 传入node 而不是 value 我们就能实现 O(1) 删除
        :return:
        """
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """相比单链表独有的反序遍历"""
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode
```

时间复杂度：

| 循环双端链表操作                       | 平均时间复杂度 |
| -------------------------------------- | -------------- |
| cdll.append(value)                     | O(1)           |
| cdll.appendleft(value)                 | O(1)           |
| cdll.remove(node)，注意这里参数是 node | O(1)           |
| cdll.headnode()                        | O(1)           |
| cdll.tailnode()                        | O(1)           |

注意删除时的参数。

为何单链表不能以此方式删除节点？因为单链表的节点只记录了后节点，而不知道前节点是谁，因此无法直接完成删除操作。

### LRU Cache

使用一个 python内置的dict 和一个上面已经实现的循环双端链表实现LRU，使用**双向链表**去记录哈希表中键的顺序，使用dict保存双向链表的各个节点（封装了key、value数据）。

为何使用循环双端链表：从dict中取得节点后可以直接以O(1)的复杂度从链表中删除节点。

代码实现：

```python
class LRUCache(object):
    def __init__(self, maxsize=16):
        self.maxsize = maxsize
        self.cache = {}
        self.access = CircularDoubleLinkedList()
        self.isfull = len(self.cache) >= self.maxsize

    def __call__(self, func):
        def wrapper(n):
            cachenode = self.cache.get(n)
            if cachenode is not None:  # hit
                self.access.remove(cachenode)
                self.access.append(cachenode)
                value = cachenode.value
            else:  # miss
                value = func(n)
                newnode = Node(key=n, value=value)
                self.cache[n] = newnode
                if self.isfull:  # 队列已满
                    lru_node = self.access.headnode()
                    self.access.remove(lru_node)
                    self.access.append(newnode)
                    del self.cache[lru_node.key]
                else:  # 队列未满
                    self.access.append(newnode)
                    self.isfull = len(self.cache) >= self.maxsize
            return value

        return wrapper


@LRUCache()
def fib(n):
    if n <= 2: # 1 or 2
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

参考文章：

- [How to implement LRU cache using HashMap and Doubly Linked List](https://medium.com/@krishankantsinghal/my-first-blog-on-medium-583159139237)
- [使用Python collections内置的OrderedDict实现LRU](https://docs.python.org/3.7/library/collections.html#ordereddict-objects)

## 04 队列

### 单链表实现

队列只有push和pop两个操作，因此我们首选使用具有append和popleft操作，且操作的时间复杂度均为O(1)的单链表结构实现。

实现：

```python
class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:  # 注意判断队列是否已满
            raise FullError('queue full')
        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) <= 0:  # 注意判断队列是否为空
            raise Emptyrror('queue empty')
        return self._item_linked_list.popleft()
```

### 数组实现

使用预先分配固定内存的顺环数组实现队列需要两个指向首尾的指针，在push与pop操作的同时移动首尾指针。

注意head指针（或tail也可）指向的是当前最后一个元素的后面一个索引位置，因此数组的大小计算方式为head - tail，~~实际上数组的最大大小比分配给数组的空间小1，即head指向的位置永远都是空的（为了能够判断数组大小）~~，此时head和tail指针可以在一个循环过后重叠（因两个指针的值没有大小限制）。

```python
class ArrayQueue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value
```

### 用list实现队列

队列需要从头删除，向尾部增加元素，也就是 list.remove(0, element) 和 list.append(element)， list.remove(0, element) 会导致所有list元素前移，O(n)复杂度。append 平均复杂度倒是O(1)，但如果内存不够还要重新分配内存。

### 双端队列 Double ended Queue

利用双端链表的以下方法：

- append
- appendleft
- headnode()
- tailnode()
- remove(node) # O(1)

即可实现 append(), appendleft(), popleft(), pop() 等 O(1)复杂度的操作。 

实现：

```python
class DoubleEndedQueue(CircularDoubleLinkedList):

    def pop(self):
        if self.tailnode() is self.root:
            raise Exception('LinkedList is empty.')
        tailnode = self.tailnode()
        return self.remove(tailnode)

    def popleft(self):
        if self.headnode() is self.root:
            raise Exception('LinkedList is empty.')
        headnode = self.headnode()
        return self.remove(headnode)
```

## 05 栈

ADT：能方便在尾部增减元素，且时间复杂度低。

使用双端链表与数组实现的pop、push操作时间复杂度均为O(1)。

### 使用双端链表实现

实现：

```python
class Stack:
    def __init__(self):
        self.deque = DoubleEndedQueue()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque) == 0
```

### 使用数组实现

实现：

```python
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
```

## 06 算法分析

主要关注渐进上界，使用大O符号表示在最糟糕的情况下算法的运行时间。

### 常用时间复杂度

| O       | 名称         | 举例               |
| ------- | ------------ | ------------------ |
| 1       | 常量时间     | 一次赋值           |
| log*n*  | 对数时间     | 折半查找           |
| n       | 线性时间     | 线性查找           |
| nlog*n* | 对数线性时间 | 快速排序           |
| n^2^    | 平方         | 两重循环           |
| n^3^    | 立方         | 三重循环           |
| 2^n^    | 指数         | 递归求斐波那契数列 |
| *n*!    | 阶乘         | 旅行商问题         |

### 常见复杂度增长趋势

![function_growth](assets/function_growth.png)

## 07 哈希表

数据依旧保存在数组中，但通过哈希函数计算的下标访问（注意取模过程）。查找、访问、删除元素的时间复杂度均为O(1)。

### 冲突及解决策略

1. 链接法：冲突时将对应的槽编程链式机构。
2. 开放寻址法：当槽被占用时，重新计算下一个可用的槽。
   - 线性探查(linear probing): 当一个槽被占用，找下一个可用的槽。  $ h(k, i) = (h^\prime(k) + i)  \% m, i = 0,1,...,m-1 $
   - 二次探查(quadratic probing): 当一个槽被占用，以二次方作为偏移量。 $ h(k, i) = (h^\prime(k) + c_1 + c_2i^2) \% m , i=0,1,...,m-1 $
   - 双重散列(double hashing): 重新计算 hash 结果。 $ h(k,i) = (h_1(k) + ih_2(k)) \% m $
3. Cpython 解决哈希冲突的方式：j = ((5*j) + 1) **mod** 2**i

### 扩容

#### 装载因子

已经使用的槽数除以哈希表大小，通常当负载因子开始超过 0.8 的时候，就要新开辟空间并且重新进行散列。

#### 重哈希

重新开辟一块新的空间，把原来哈希表里不为空槽的数据重新插入到新的哈希表里（迭代遍历原来的哈希表），插入方式和哈希表之前的插入方式一样。

python3.3 的扩容策略是扩大为已经使用的槽数目的两倍。

### 使用数组实现ADT

实现：

```python
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
```

#### 关键理解

1. 数组保存的对象以及slot的不同值。
2. 通过hash计算数组下标。
3. 在数组中查找key。
4. 在数组中查找可供key插入的位置。
5. 重哈希。
6. 增减元素时length的更新。

## 08 字典

python 内置的 dict 是用哈希表实现的。

使用哈希表实现dict：

```python
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
```

主要是几个专门的方法，基本的元素操作方法已经在哈希表中实现。

注意items等方法在python3中返回的是迭代器。

### Hashable

作为 dict 的 key 必须是可哈希的，也就是说不能是 list 等可变对象。

> An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal must have the same hash value.
>
> Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.
>
> All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal (except with themselves), and their hash value is derived from their id().

[可变对象和不可变对象的区别](https://zhuanlan.zhihu.com/p/39566815)

## 09 集合

集合的底层也是由哈希表实现的，即把所有的key的value都置为True（1）。额外的操作方法是实现数学上的集合运算（交并补），我们可以通过重载python的内置运算符实现。

因为集合的底层由哈希表实现，因此集合的元素也要求为hashable。

### ADT实现

```python
class SetADT(HashTable):

    def add(self, key):
        # 集合其实就是一个 dict，只不过我们把它的 value 设置成 1
        return super(SetADT, self).add(key, True)

    def __and__(self, other_set):
        """交集 A&B"""
        new_set = SetADT()
        for element in self:
            if element in other_set:
                new_set.add(element)
        return new_set

    def __sub__(self, other_set):
        """差集 A-B"""
        new_set = SetADT()
        for element in self:
            if element not in other_set:
                new_set.add(element)
        return new_set

    def __or__(self, other_set):
        """并集 A|B"""
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other_set:
            new_set.add(element_b)
        return new_set

    def __xor__(self, other_set):
        """对称差 A^B"""
        union_set = self.__or__(other_set)
        inter_set = self.__and__(other_set)
        new_set = union_set.__sub__(inter_set)
        return new_set
```

### python frozenset

在 python 里还有一个 frozenset，看它的名字就知道这种也是集合，但是它的内容是无法变动的。一般我们使用 它的常见就是用一个可迭代对象初始化它，然后只用来判重等操作。

### BloomFilter布隆过滤器

需要快速判断某个元素是否属于集合，且集合数据量相当时的解决方案（以URL字符串为例）：

1. 将访问过的URL保存到数据库。
2. 用HashSet将访问过的URL保存起来。那只需接近O(1)的代价就可以查到一个URL是否被访问过了
3. URL经过MD5或SHA-1等单向哈希后再保存到HashSet或数据库。
4. Bit-Map方法。建立一个BitSet，将每个URL经过一个哈希函数映射到某一位。

缺陷（数据量相当大时）：

1. 数据量变得非常庞大后关系型数据库查询的效率会变得很低。
2. 太消耗内存。
3. 由于字符串经过MD5处理后的信息摘要长度只有128Bit，SHA-1处理后也只有160Bit，因此方法3比方法2节省了好几倍的内存。
4. 耗内存是相对较少的，但缺点是单一哈希函数发生冲突的概率太高。

#### Bloom Filter 算法

在允许小概率出错的前提下，可使用 Bloom Filter 算法：

创建一个m位BitSet，先将所有位初始化为0，然后选择k个不同的哈希函数。第i个哈希函数对字符串str哈希的结果记为h（i，str），且h（i，str）的范围是0到m-1 。

##### 加入字符串过程

对于字符串str，分别计算h（1，str），h（2，str）…… h（k，str）。然后将BitSet的第h（1，str）、h（2，str）…… h（k，str）位设为1。这样就将字符串str映射到BitSet中的k个二进制位了。

![img](assets/2011010219003441.jpg)

##### 检查字符串是否存在的过程

对于字符串str，分别计算h（1，str），h（2，str）…… h（k，str）。然后检查BitSet的第h（1，str）、h（2，str）…… h（k，str）位是否为1，若其中任何一位不为1则可以判定str一定没有被记录过。若全部位都是1，则“认为”字符串str存在。

- 若一个字符串对应的Bit不全为1，则可以肯定该字符串一定没有被Bloom Filter记录过。
- 但是若一个字符串对应的Bit全为1，实际上是不能100%的肯定该字符串被Bloom Filter记录过的。

##### 删除字符串过程

字符串加入了就被不能删除了，因为删除会影响到其他字符串。实在需要删除字符串的可以使用Counting bloomfilter(CBF)，这是一种基本Bloom Filter的变体，CBF将基本Bloom Filter每一个Bit改为一个计数器，这样就可以实现删除字符串的功能了。

选择k个不同的哈希函数比较麻烦，一种简单的方法是选择一个哈希函数，然后送入k个不同的参数。

## 10 递归

阶乘函数：

```python
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
```

特点：

- 递归必须包含一个基本的出口(base case)，否则就会无限递归，最终导致栈溢出。比如这里就是 n == 0 返回 1。
- 递归必须包含一个可以分解的问题(recursive case)。 要想求得 fact(n)，就需要用 n * fact(n-1)。
- 递归必须必须要向着递归出口靠近(toward the base case)。 这里每次递归调用都会 n-1，向着递归出口 n == 0 靠近。

### 用栈模拟递归

```python
from collections import deque


class Stack(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_use_stack(n):
    s = Stack()
    while n > 0:    # 不断将参数入栈
        s.push(n)
        n -= 1

    while not s.is_empty():    # 参数弹出
        print(s.pop())
```

### 尾递归

递归调用放在函数的最后。[参考文章](http://www.ruanyifeng.com/blog/2015/04/tail-call.html)

函数调用会在内存形成一个"调用记录"，又称"调用帧"（call frame），保存调用位置和内部变量等信息。如果在函数A的内部调用函数B，那么在A的调用记录上方，还会形成一个B的调用记录。等到B运行结束，将结果返回到A，B的调用记录才会消失。如果函数B内部还调用函数C，那就还有一个C的调用记录栈，以此类推。所有的调用记录，就形成一个["调用栈"](http://zh.wikipedia.org/wiki/%E8%B0%83%E7%94%A8%E6%A0%88)（call stack）。

尾调用由于是函数的最后一步操作，所以不需要保留外层函数的调用记录，因为调用位置、内部变量等信息都不会再用到了，只要直接用内层函数的调用记录，取代外层函数的调用记录就可以了。

尾递归的实现，往往需要改写递归函数，确保最后一步只调用自身。做到这一点的方法，就是把所有用到的内部变量改写成函数的参数。

python 默认不支持尾递归优化（见延伸阅读），不过一般尾递归我们可以用一个迭代来优化它。

### 汉诺塔问题

假设有 A、B、C 三个塔，A 塔有 N 块盘，目标是把这些盘全部移到 C 塔。那么先把 A 塔顶部的 N-1块盘移动到 B 塔（借助C塔），再把 A 塔剩下的大盘移到 C，最后把 B 塔的 N-1 块盘移到 C（借助A塔）。

```python
def move(n, source, dest, inter):
    if n >= 1:
        move(n-1, source, inter, dest)
        print('move {} --> {}'.format(source, dest))
        move(n-1, inter, dest, source)

move(3, 'A', 'C', 'B')

# 输出
"""
move A --> C
move A --> B
move C --> B
move A --> C
move B --> A
move B --> C
move A --> C
"""
```

## 11 线性查找与二分查找

### 线性查找

从头找到尾，符合条件了就返回。

```python
number_list = list(range(8))

def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1

assert linear_search(5, number_list) == 5
```

### 二分查找

#### 等值查找

```python
def binary_search(sorted_array, val):
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array) - 1

    while beg <= end:
        mid = beg + (end-beg)//2
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] < val:
            beg = mid + 1
        else:
            end = mid - 1
    return -1


def test_binary_search():
    a = list(range(10))

    # 正常值
    assert binary_search(a, 1) == 1
    assert binary_search(a, -1) == -1

    # 异常值
    assert binary_search(None, 1) == -1

    # 边界值
    assert binary_search(a, 0) == 0

```

### 求上下界

用二分查找法求下界：

```python
def lower_bound(array, value):  # 返回[first, last)内第一个不小于value的值的位置
    first = 0
    last = len(array)
    while first < last:  # 搜索区间[first, last)不为空
        mid = first + (last - first) // 2  # 防溢出
        if array[mid] < value:
            first = mid + 1
        else:
            last = mid
    return first  # last也行，因为[first, last)为空的时候它们重合


def test_binary_search():
    a = list(range(10))

    assert lower_bound(a, 3) == 3
    assert lower_bound(a, 10) == 10
    assert lower_bound(a, 9) == 9

    assert lower_bound(a, 0) == 0
    assert lower_bound(a, 9) == 9

```

参考文章：[二分查找有几种写法？它们的区别是什么？](https://www.zhihu.com/question/36132386)

## 12 基本排序算法

### 冒泡排序

#### 原理

![img](assets/849589-20171015223238449-2146169197.gif)

- 从第一个元素开始比较相邻的元素。如果第一个比第二个大，就交换它们的位置；
- 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
- 重复对不包括已选出的最大元素的元素执行以上步骤，直到排序完成。

#### 代码实现

重点理解两层迭代的范围：

- 第一层迭代为比较轮数，每一轮都会选出一个当前轮最大值，只剩一个元素未排序时不需要再比较，因此为n-1次。
- 第二层迭代为每一轮比较的下标范围，比较从第一个值开始（下标0）并比较当前位置值与下一位置值，因此不会迭代到最后一个元素，所以次数为n-1，每一轮已经选出的最大值不再比较，因此最后的总次数为n-1-i。

需要考虑的中间值：元素数量n

```python
def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):  # 需要减去i是因为每一轮冒泡最大的元素都会冒泡到最后，无需再比较
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]

```

#### 算法分析

不管初始序列中的元素如何分布，为了使大小为 n 的序列有序，将执行 n-1 轮的排序，第一轮进行 n-1 次前后比较，第二轮进行 n-2 次，以此类推，最后的第 n-1 轮进行 1 次比较，因此总的次数为前 n-1 个数之和，计算结果为1/2n^2^-1/2n，即时间复杂度为O(n^2^)。

最好与最差情况下元素交换的次数会有所区别。

### 选择排序

#### 原理

![img](assets/849589-20171015224719590-1433219824.gif)

1. 将序列分为无序区和有序区，初始状态的无序区为[0,..,,n-1]，有序区为空；
2. 第i轮排序(轮数从0开始)开始时，当前有序区和无序区分别为[0..i]和[[i..n-1]。该轮排序将第1个元素[i]假设为无序区的最小值，从第二个元素开始比较选出当前无序区中最小的元素[k]，将它与无序区的第1个元素[i]交换，有序区增加1个元素，无序区减少一个元素；
3. n-1轮之后，无序区还有一个最大元素，此时整个序列已经有序，排序结束。

#### 代码实现

重点理解两层迭代的范围：

- 第一层迭代为比较轮数，每一轮都会选出一个当前轮最小值摆放到当前下标，只剩一个元素未排序时不需要再比较，因此为n-1次。
- 第二层迭代为比较的下标范围，从当前下标的下一个元素到序列的最后一个元素（下标为n-1），因此范围为range(i + 1, n)。

n个记录的选择排序可经过n-1轮选择排序得到有序结果。

如何寻找最值：假设当前下标为最小下标，若有更小值，则以该值下标为最小下标。

需要考虑的中间值：元素数量n和临时变量min_index。

```python
def selection_sort(seq):
    n = len(seq)
    for i in range(n - 1): 
        min_index = i  # 假设当前下标的元素是最小的
        for j in range(i + 1, n):  # 从i之后开始找到最小的元素，一直找到最后一个元素
            if seq[j] < seq[min_index]:
                min_index = j  # 循环结束后得到最小元素的下标
        if min_index != i:  # 循环结束后如果最小的元素不是当前下标的元素，则交换
            seq[i], seq[min_index] = seq[min_index], seq[i]

```

#### 算法分析

比较次数与冒泡排序相同，无论什么序列进行排序都是O(n^2^)的时间复杂度，不占用额外的内存空间。

相比冒泡排序，交换元素的次数会更少一些，因此性能更好。

### 插入排序

#### 原理

![img](assets/849589-20171015225645277-1151100000.gif)

1. 假定序列的第一个元素已经有序；
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
3. 如果已排序序列中的当前扫描元素大于新元素，将该元素移到下一位置；
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5. 将新元素插入到该位置之后；
6. 重复步骤2~5。

#### 代码实现

第一层迭代的范围：进行比较的下标范围，从第二个值开始到最后一个值结束，因此为 range(1, n)。

如何取出值：将当前位置的值赋给临时变量value，最后再将value值放到往前比较停止时的位置。

如何通过while循环往前比较且在特定条件停止：将前一位置的值赋值到当前比较位置，再通过自减将当前比较位置往前移。

```python
def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):  # 元素为0个或1个时是有序的
        value = seq[i]  # 取出当前位置元素的值
        pos = i  # 找到这个值的合适位置，使得前边的数组有序 [0,i] 有序
        while pos > 0 and value < seq[pos - 1]:  # 比较取出值与前面的元素值，如果取出值更小，继续前移
            seq[pos] = seq[pos - 1]  # 将比较过的值往后移
            pos -= 1  # 继续往前比较（前移取出值的位置）
        seq[pos] = value  # 将取出的值插入到当前位置

```

#### 算法分析

对于大小为 n 的序列依然需要进行 n-1 轮排序，每一轮的比较次数根据序列元素分布情况会有所区别，最大比较次数下时间复杂度为O(n^2^)，最好情况下每一轮只需比较一次。

插入排序在实现上，通常采用in-place原地排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

### 希尔排序

希尔排序是插入排序的改进版，又叫做**缩小增量排序**。

#### 原理

![img](assets/849589-20180331170017421-364506073.gif)

希尔排序是把序列按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的元素越来越多，当增量减至1时，整个序列恰被分成一组，此时再执行一个直接插入排序，算法便终止。

#### 代码实现

```python
def shell_sort(seq):
    n = len(seq)
    group = 2  # 每次将序列分成n/2^i个子序列（i从1开始递增）
    gap = n // group  # 子序列数量，同时也是下标增量值
    while gap > 0:  # 增量值最终递减到1
        # 对每个子序列进行插入排序,共进行gap轮
        for i in range(gap):
            # 对当前序列进行插入排序，从当前序列的第二个元素即i+gap开始比较（初始元素下标为i）
            for j in range(i + gap, n, gap):  # 以gap为step获取遍历序列
                value = seq[j]
                pos = j

                while pos >= gap and value < seq[pos - gap]:  # pos-gap>=0,因此pos>=gap
                    seq[pos] = seq[pos - gap]
                    pos -= gap

                seq[pos] = value
        gap = gap // group

```

#### 算法分析

尽管希尔排序是执行多次的插入排序，并在最后对所有元素执行了一次插入排序，但实际上总的操作次数要好于插入排序。

希尔排序具体的时间复杂度分析十分复杂，但总时间复杂度介于 O(n) 和 O(n2) 之间，核心在于间隔序列的设定。

## 13 高级排序算法

### 分治法

分治法在每层递归时有三个步骤：

- **分解**原问题为若干子问题，这些子问题是原问题的规模最小的实例
- **解决**这些子问题，递归地求解这些子问题。当子问题的规模足够小，就可以直接求解
- **合并**这些子问题的解成原问题的解

### 归并排序

![img](assets/849589-20171015230557043-37375010.gif)

把数组递归成只有单个元素的数组，之后再不断两两合并，最后得到一个有序数组。这里的递归基本条件就是只包含一个元素的数组。

- **分解**：将待排序的 n 个元素分成各包含 n/2 个元素的子序列
- **解决**：使用归并排序递归排序两个子序列
- **合并**：将两个排序好的子序列合并成一个最终的排序序列。

代码实现：

```python
def merge_sort(seq):
    n = len(seq)
    if n <= 1:
        return seq
    else:
        mid = n // 2
        # 递归的对左右部分进行分割排序
        left_part = merge_sort(seq[:mid])
        right_part = merge_sort(seq[mid:])

        # 合并排序后的左右部分
        new_seq = merge_two_part(left_part, right_part)
        return new_seq

```

#### 归并两个有序数组

分别在两个数组中设置两个迭代指针，循环的比较指针所指的值并前移指针（while嵌套if...else结构）。

创建一个新列表用于存放两个列表比较时的较小值。

注意循环终止后将没迭代完的数组存入列表。

```python
def merge_two_part(sorted_a, sorted_b):
    length_a = len(sorted_a)
    length_b = len(sorted_b)
    a = b = 0
    new_seq = list()

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_seq.append(sorted_a[a])
            a += 1
        else:
            new_seq.append(sorted_b[b])
            b += 1

    if a < length_a:
        new_seq.extend(sorted_a[a:])
    else:
        new_seq.extend(sorted_b[b:])=

```

#### 算法分析

类似快速排序，但需要额外的空间。因为每次都是序列中间进行分割，通过logn次可将序列分割完毕，合并时需要遍历序列所有元素，不管元素在什么情况下都要做这些步骤，所以花销的时间是不变的，因此该算法的最优、最差及平均时间复杂度都为O(n*logn)。

归并的空间复杂度就是那个临时的数组和递归时压入栈的数据占用的空间：n + logn；所以空间复杂度为: O(n)

### 快速排序

![img](assets/849589-20171015230936371-1413523412.gif)

平均情况下表现最优。

步骤：

- 选择基准值 pivot 将数组分成两个子数组：小于基准值的元素和大于基准值的元素。这个过程称之为 partition。
- 对这两个子数组进行快速排序。
- 返回基准值和子数组的合并结果。

#### 基础版本

```python
def quicksort(array):
    if len(array) < 2:  # 递归出口，空数组或者只有一个元素的数组都是有序的
        return array
    else:
        pivot = array[0]
        less_part = [i for i in array[1:] if i < pivot]
        great_part = [i for i in array[1:] if i >= pivot]
        return quicksort(less_part) + [pivot] + quicksort(great_part)

```

缺点：

- 需要额外的存储空间，最好可以 inplace 原地排序。
- partition 操作每次都要两次遍历整个数组。

#### 改良版本

- 从数列中挑出一个元素，称为 “基准”（pivot）；
- 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
- 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

```python
def quicksort_inplace(array, beg, end):  # 注意这里我们都用左闭右开区间，end 传入 len(array)
    if beg < end - 1:
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot + 1, end)	

```

注意其执行条件，当执行快排的序列元素个数小于或等于1时，序列已经是有序的，不需要再进行递归的快排操作。当程序递归执行到所有待执行快排的子序列都已经有序时，整个序列也是有序的，程序执行完毕退出。

Partition图示：

**注意递归执行快排的序列不再包括前一次partition操作的pivot值。**

![../_images/partitionB.png](assets/partitionB.png)

Partition操作：

while True 无限循环，通过比较左右指针决定break结束循环还是交换指针所在位置的值。

![../_images/partitionA.png](assets/partitionA.png)

```python
def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1    # 开区间，最后一个元素位置是 end-1     [0, end-1] or [0: end)，括号表示开区间

    while True:
        # 从左边找到比 pivot 大的
        while left <= right and array[left] < pivot:
            left += 1
        # 从右边找到比 pivot 小的, 注意停止循环的条件
        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right   # 新的 pivot 位置

```

设置左右指针，分别从两边向中间迭代并交换位置，最后right指针停在应与piviot交换的位置。

#### 算法分析

当选定pivot的值为中位数，即每次Partition操作都从序列中间执行时，执行logn次即可将序列分割完毕(考虑二分查找)，每一次分割操作需要遍历序列所有元素与pivot值比较，需要操作n次，总的时间复杂度为O(n*logn).

但极端情况下，比如序列已经是有序的，若每次选序列首位的元素作为pivot，需要执行n次partition操作才能将序列分割完毕，此时的时间复杂度为O(n^2^).

一种解决方案是通过取**序列首尾及中间三个数中的中位数**作为pivot，这样能有效的避免最差情况出现。

就地快速排序使用的空间是O(1)的，也就是个常数级；而真正消耗空间的就是递归调用了，因为每次递归就要保持一些数据；
最优的情况下空间复杂度为：O(logn) ，每一次都平分数组的情况；
最差的情况下空间复杂度为：O( n ) ，退化为冒泡排序的情况。

### 无序数组寻找第 k 大的数字

```python
def partition_desc(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1  # 开区间，最后一个元素位置是 end-1     [0, end-1] or [0: end)，括号表示开区间

    while True:
        # 从左边找到比 pivot 大的
        while left <= right and array[left] >= pivot:
            left += 1
        # 从右边找到比 pivot 小的
        while right >= left and array[right] < pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right  # 新的 pivot 位置


def findkth(array, beg, end, k):
    index = partition_desc(array, beg, end)
    if index == k - 1:
        return array[index]
    elif index < k - 1:
        return findkth(array, index + 1, end, k)
    else:
        return findkth(array, beg, index, k)

```

### 排序总结

稳定性：

- **稳定**：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
- **不稳定**：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。

| 排序算法   | 最坏时间复杂度 | 平均时间复杂度 | 最好时间复杂度 | 稳定性 | 空间复杂度      |
| ---------- | -------------- | -------------- | -------------- | ------ | --------------- |
| 冒泡排序   | O(n^2^)        | O(n^2^)        | O(n)           | 稳定   | O(1)            |
| 选择排序   | O(n^2^)        | O(n^2^)        | O(n^2^)        | 不稳定 | O(1)            |
| 插入排序   | O(n^2^)        | O(n^2^)        | O(n)           | 稳定   | O(1)            |
| 希尔排序   | O(n^2^)        | O(n^1.3^)      | O(n)           | 不稳定 | O(1)            |
| 归并排序   | O(n*log~2~n)   | O(n*log~2~n)   | O(n*log~2~n)   | 稳定   | O(n)            |
| 快速排序   | O(n^2^)        | O(n*log~2~n)   | O(n*log~2~n)   | 不稳定 | O(log~2~n)~O(n) |
| 二叉树排序 | O(n^2^)        | O(n*log~2~n)   | O(n*log~2~n)   | 不稳定 | O(n)            |
| 堆排序     | O(n*log~2~n)   | O(n*log~2~n)   | O(n*log~2~n)   | 不稳定 | O(1)            |

## 14 树与二叉树

二叉树的相关概念：

- 节点深度(depth): 节点对应的 level 数字
- 树的高度(height): 二叉树的高度就是 level 数 + 1，因为 level 从 0开始计算的
- 树的宽度(width): 二叉树的宽度指的是包含最多节点的层级的节点数
- 树的 size：二叉树的节点总个数。

一棵 size 为 n 的二叉树高度最多可以是 n，最小的高度是 ⌊lgn⌋+1

满二叉树：

![img](assets/full_binary_tree.png)

完美二叉树：

![img](assets/perfect_binary_tree.png)

完全二叉树：

![img](assets/complete_binary_tree.png)

### 二叉树的表示

首先定义节点：

```python
class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

```

定义root节点作为入口即可定义一个二叉树：

```python
class BinTree(object):
    def __init__(self, root=None):
        self.root = root

```

#### 构造二叉树

以字典表示单个节点的信息并保存在列表中，通过列表中的data信息构造节点并将节点对象放入另一字典中，最后根据列表中的孩子信息从字典中取出node节点并给孩子和根节点复制，对类进行初始化返回实例对象。

```python
@classmethod
def build_from(cls, node_list):
    """通过节点信息构造二叉树
    第一次遍历使用data数据分别构造 node 节点并存入字典，node.left和node.right仍然为None
    第二次遍历从字典中取出node节点并给 root 和 孩子赋值(用node赋值)
    最后用 root 节点初始化这个类并返回一个实例对象

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

```

### 二叉树的遍历

二叉树是一种递归结构，可以直接用递归的方式来遍历。

分为三种遍历方式:

- 先(根)序遍历: 先处理根，之后是左子树，然后是右子树
- 中(根)序遍历: 先处理左子树，之后是根，最后是右子树
- 后(根)序遍历: 先处理左子树，之后是右子树，最后是根

前中后序三种遍历方法对于左右结点的遍历顺序都是一样的（先左后右），唯一不同的就是根节点的出现位置，即处理时机。

对于一个子树[A,B,C]，A是父节点，B是左子，C是右子：
先序：A B C
中序：B A C
后序：B C A

可以此递推到所有子树。

#### 递归实现

先序遍历：

```python
def preorder_trav(self, node):
    """先序遍历"""
    if node is not None:
        print(node.data)  # 递归函数里先处理根
        self.preorder_trav(node.left)  # 递归处理左子树
        self.preorder_trav(node.right)  # 递归处理右子树

```

中序遍历及后序遍历：移动print函数位置即可。

#### 非递归实现

使用堆栈实现遍历：

- 遇到一个节点，就把它压栈，并去遍历它的左子树；
- 当左子树遍历结束后，从站定弹出这个节点并访问它；
- 然后按其右指针再去遍历该节点的右子树，回到第一步。

```python
def preorder_trav_use_stack(self, node):
    s = Stack()
    while node or not s.empty():  # 循环重复整个过程
        while node:  # 不断往左子树遍历
            print(node.data) # 先序处理节点
            s.push(node)  # 第一次遇到节点
            node = node.left
        if s.empty() is not None:  # 左子树为空时回到上一节点往右子树遍历
            node = s.pop()  # 回到上一个节点的方式，第二次遇到节点
            node = node.right  # 从上一个节点的右边开始遍历

```

**二叉树的遍历，不会往回走（即不能这么理解），而是直接从上一个节点往右子树方向开始遍历。**

规律为：当前结点curr不为None时，每一次循环将当前结点curr入栈；当前结点curr为None时，则出栈一个结点，且打印出栈结点的value值。整个循环在stack和curr皆为None的时候结束。

两层循环：里面一层是不停的往左遍历，外面一层是不断的在左子树没有节点时回到上一节点往右子树遍历。

### 二叉树层序遍历

使用队列实现：

```python
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

```

使用列表实现：

```python
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

```

### 反转二叉树

```python
def reverse(self, node):
    """
    和遍历操作类似，递归进行交换
    :param node:
    :return:
    """
    if node is not None:
        node.left, node.right = node.right, node.left  # 交换在函数中的位置前后都可以
        self.reverse(node.left)
        self.reverse(node.right)

```

## 15 堆和堆排序

### 堆的概念

堆是一种完全二叉树，有最大堆和最小堆两种。

- 最大堆: 对于每个非叶子节点 V，V 的值都比它的两个孩子大，称为 最大堆特性(heap order property) 最大堆里的根总是存储最大值，最小的值存储在叶节点。
- 最小堆：和最大堆相反，每个非叶子节点 V，V 的两个孩子的值都比它大。最小堆里的根总是存储最小值，最大的值存储在叶节点。

### 堆的操作

- 插入新的值。插入时需要维持堆的特性，**每次从底层最右边的节点后插入**，需要 sift-up 操作。
- **获取并移除根节点的值**。每次我们都可以获取最大值或者最小值，**然后把底层最右边的节点值替换到 root 节点**之后执行 sift-down 操作。

### 堆的表示

因为堆是完全二叉树没有间隙，所以可用一维的数组来表示二维的堆。

对于数组里的一个下标 i，我们可以得到它的父亲和孩子的节点对应的下标：

```
parent = (i-1) // 2   # 取整
left = 2 * i + 1
right = 2 * i + 2

```

超出数组下标范围表示没有对应的孩子节点。

### 实现一个最大堆

关键是需要实现add和extract方法，以及对应方法中为了维持堆的特性进行的sift操作。

add 方法每次从底层最右边的节点后插入新节点，进行 sift-up 操作。

extract 方法每次获取根节点的最大值，然后把底层最右边的节点值替换到 root 节点，之后执行 sift-down 操作。

```python
class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value

        self._count += 1
        self._siftup(self._count - 1)  # 维持堆的特性

    def _siftup(self, ndx):
        if ndx > 0:
            parent = (ndx - 1) // 2
            if self._elements[ndx] > self._elements[parent]:  # 如果插入的值大于 parent，一直交换
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]  # 保存 root 值
        self._count -= 1
        self._elements[0] = self._elements[self._count]  # 最右下的节点放到root后siftDown
        self._siftdown(0)  # 维持堆特性
        return value

    def _siftdown(self, ndx):
        left = ndx * 2 + 1
        right = ndx * 2 + 2
        # 找出当前节点及左右子节点中的最大值，与当前节点交换位置，并递归地对换下去的节点执行siftdown操作
        largest = ndx
        if left < self._count and self._elements[left] > self._elements[largest] and right < self._count and \
                self._elements[left] >= self._elements[right]:
            largest = left
        elif left < self._count and self._elements[left] > self._elements[largest] and right >= self._count:
            largest = left
        elif right < self._count and self._elements[right] > self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)
```

### 实现一个最小堆

实现同最大堆基本相同，仅节点的比较条件不同。

```python
class MinHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)

    def _siftup(self, ndx):
        if ndx > 0:
            parent = (ndx - 1) // 2
            if self._elements[ndx] < self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = (ndx * 2) + 1
        right = (ndx * 2) + 2
        # 找出当前节点及左右子节点中的最小值，与当前节点交换位置，并递归地对换下去的节点执行siftdown操作
        smallest = ndx
        if left < self._count and self._elements[left] < self._elements[smallest] and right < self._count and \
                self._elements[left] <= self._elements[right]:
            smallest = left
        elif left < self._count and self._elements[left] < self._elements[smallest] and right >= self._count:
            smallest = left
        elif right < self._count and self._elements[right] < self._elements[smallest]:
            smallest = right
        if smallest != ndx:
            self._elements[ndx], self._elements[smallest] = self._elements[smallest], self._elements[ndx]
            self._siftdown(smallest)
```

### 实现堆排序

将无序序列中的元素依次add到同样大小的堆中，然后再依次extract堆顶的元素，即得到了有序的序列。

#### 倒序排序

```python
def heapsort_reverse(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    res = []
    for i in range(length):
        res.append(maxheap.extract())
    return res
```

#### 正序排序

```python
def heapsort(array):
    length = len(array)
    minheap = MinHeap(length)
    for i in array:
        minheap.add(i)
    res = []
    for i in range(length):
        res.append(minheap.extract())
    return res
```

**T ( N ) = O ( N log N )**
缺点：**需要额外O(N)空间，并且复制元素需要时间。**

#### 原地堆排序

以最大堆实现升序排列为例：

对于最大堆来说，根节点的元素总是最大的，因此，如果每次都把根节点的元素和最后的元素互换位置，并将堆的元素计数减一，然后再对堆的当前根节点进行一次sift down，那么最后一个元素就是整个数组的最大值，不断进行这样的操作，利用堆的性质，就可以让一个数组最终从小到大排序。

```python
def heapsort_inplace(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    while maxheap._count > 1:
        maxheap._elements[0], maxheap._elements[maxheap._count - 1] = maxheap._elements[maxheap._count - 1], maxheap._elements[0]
        maxheap._count -= 1
        maxheap._siftdown(0)
    return list(maxheap._elements)
```



### Python 里的 heapq 模块

#### heapq 的特性

使用对所有的k都满足 `heap[k] <= heap[2*k+1]` 和 `heap[k] <= heap[2*k+2]` 条件的数组实现，从0开始计算下标。最小的元素总是为第一个元素即 `heap[0]`，根节点。heapq实现的是最小堆。

创建一个堆有两种方法：

- 使用一个初始化为`[]`的list作为堆。
- 使用 [`heapify()`](#heapq.heapify)方法将已填充元素的list转换为堆。

#### heapq 的常用方法

- `heapq.heappush`(*heap*, *item*)

  将item push到堆中，并维持堆的特性不变。

- `heapq.heappop`(*heap*)

  pop 并返回堆中最小的元素，并维持堆的特性不变。如果堆已空，唤起 [`IndexError`](exceptions.html#IndexError) 异常。使用 `heap[0]` 在不 pop 的情况获取最小元素。

- `heapq.heappushpop`(*heap*, *item*)

  Push *item* 到堆中，然后从堆中 pop 出最小值。比单独调用 [`heappush()`](#heapq.heappush) 以及 [`heappop()`](#heapq.heappop)效率更高。

- `heapq.heapify`(*x*)

  以线性时间在原地将 list *x* 转换为一个堆。

- `heapq.heapreplace`(*heap*, *item*)

  Pop 并且返回堆中的当前最小元素，然后将新的 *item* push 到堆中。操作不会改变堆的大小，因此更适合用在固定大小的堆中，比单独执行两个操作更高效。如果堆已空，唤起 [`IndexError`](exceptions.html#IndexError) 异常。

### Top K 问题

在内存有限的情况下，使用最小堆求top k 问题。

考虑使用包含k个元素的最大堆和最小堆，不断加入元素并维持堆的大小不变。先用数组的前面 k 个元素建立最大堆，然后对剩下的元素进行比对，最大堆只能**每次获取堆顶最大的一个元素**，如果我们取下一个大于堆顶的值和堆顶替换，堆底部的小数一直不会被换掉。如果下一个元素小于堆顶就替换可能会弹出最大的元素。

使用最小堆时先迭代前 k 个元素建立一个最小堆，之后的元素如果小于堆顶最小值，跳过，否则弹出堆顶元素并加入元素重新调整堆。最小堆里的元素慢慢就被替换成了最大的那些值，并且最后堆顶是最大的 topk 个值中的最小值。 （比如1000个数找10个，最后堆里剩余的是 [990, 991, 992, 996, 994, 993, 997, 998, 999, 995]，第一个 990 最小)

```python
class TopK(object):
    """获取大量元素 topk 大个元素，固定内存
    思路：
    1. 先放入元素前 k 个建立一个最小堆
    2. 迭代剩余元素：
        如果当前元素小于堆顶元素，跳过该元素（肯定不是前 k 大）
        否则替换堆顶元素为当前元素，并重新调整堆
    """
    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, value):
        if len(self.minheap) >= self.capacity:
            min_value = self.minheap[0]
            if value > min_value:
                heapq.heapreplace(self.minheap, value)  # 返回并且pop堆顶最小值，推入新的 val 值并调整堆
        else:
            heapq.heappush(self.minheap, value)  # 前面 k 个元素直接放入minheap

    def get_topk(self):
        for i in self.iterable:
            self.push(i)
        return self.minheap
```

## 16 优先级队列

#### 基本实现

将任务的优先级与任务组成tuple加入最小堆，堆中会按照tuple的第一位也就是优先级进行排序，从而实现了优先级队列。

```python
class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._minheap = MinHeap(maxsize)

    def push(self, priority, value):
        # 注意这里把这个 tuple push 进去，python 比较 tuple 从第一个开始比较
        # 这样就实现了按照优先级排序
        entry = (priority, value)
        self._minheap.add(entry)  # 入队的时候会根据 priority 维持堆的特性

    def pop(self, with_priority=False):
        entry = self._minheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return self._minheap._count == 0
```

### 进阶实现

优先级队列除了以上基础操作外，还有以下操作需要考虑：

- 排序的稳定性：如何将两个优先级相等的任务按加入队列的顺序返回？
- 在优先级相同且没有默认的任务比较顺序时元组的比较会中断。
- 如果一个任务的优先级改变了，如何将任务在堆中移动到新的位置？
- 或者如果一个等待中的任务需要删除，应该如何找到任务并从队列中移除？

#### 解决方案

##### 优先级比较问题

将任务条目作为**三元素元组**保存，分别为优先级、条目计数以及任务（priority, an entry count, and the task），每个任务的条目计数都不相同，因此仅对比元组的前两项就可以完成所有优先级条目的比较。

##### 任务的优先级更新与删除

解决该问题的关键是如何在队列中找到特定的任务，可以通过一个指向优先级队列内一个条目的字典来寻找任务（用任务名称映射优先级条目对象）。

删除条目或者改变条目的优先级很困难，因为它会打破堆的固定特性，一个可能的解决方法是将条目任务标记为已删除（**需要将表示优先级条目的元组改为列表**），然后添加一个修改过优先级的新条目。

注意在弹出优先级任务时判断任务是否为RTEMOVED，若是则循环弹出下一个最小优先级任务。

##### 实现代码

```python
import heapq
import itertools


class PriorityQueue(object):
    REMOVED = '<removed-task>'  # 被删除任务的占位字符

    def __init__(self):
        self.pq = []  # 初始化heapq所使用的list
        self.entry_finder = {}  # 任务到优先级条目的映射
        self.counter = itertools.count()  # 唯一计数器

    def add_task(self, task, priority=0):
        """添加一个新任务或者更新一个已存在任务的优先级"""
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self, task):
        """将一个已存在的任务标记为REMOVED，若未找到Raise KeyError。"""
        entry = self.entry_finder.pop(task)
        entry[-1] = PriorityQueue.REMOVED

    def pop_task(self):
        """删除并返回最小优先级任务，如果队列已空Raise KeyError"""
        while self.pq:  # 循环直到弹出值不为REMOVED的task才返回
            priority, count, task = heapq.heappop(self.pq)
            if task is not PriorityQueue.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def is_empty(self):
        return len(self.entry_finder) == 0
```

## 17 二叉查找树

### 二叉查找树定义

二叉查找树是这样一种二叉树结构，它的每个节点包含一个 key 和它附带的数据，对于每个内部节点 V：

- 所有 key 小于 V 的都被存储在 V 的左子树
- 所有 key 大于 V 的都存储在 V 的右子树

![img](assets/bst.png)

**如果中序遍历二叉树，输出的顺序正好是有序的。**

BST的节点结构定义：

```python
class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right
```

### 构造一个BST

```python
class BST(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}
        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTNode(key, value=key)   # 这里值暂时用 和 key一样的

        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            if node_dict['is_root']:
                root = node
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            cls.size += 1
        return cls(root)


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
bst = BST.build_from(NODE_LIST)
```

### BST 操作

主要有两个操作：查找，插入。

#### 查找

使用递归的方式进行查找，对于待查找的节点 search_key，从根节点开始，如果 search_key 大于当前 key，就去右子树查找，否则去左子树查找。 一直到找到key相等的节点或当前节点是 None 了说明没找到对应 key。

```python
def _bst_search(self, subtree, key):
    if subtree is None:
        return None
    elif key < subtree.key:
        return self._bst_search(subtree.left, key)  # 递归搜索左子节点
    elif key > subtree.key:
        return self._bst_search(subtree.right, key)  # 递归搜索右子节点
    else:
        return subtree

def get(self, key, default=None):
    node = self._bst_search(self.root, key)  # 所有查找均从根节点开始
    if node is None:
        return default
    else:
        return node.value
```

#### 获取最大和最小key的节点

从根节点开始递归查找最值节点，小值就一直向着左子树找，最大值一直向右子树找。

```python
def _bst_min_node(self, subtree):
    if subtree is None: # 当根节点为None时，返回None
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
```

#### 插入

从根节点开始尝试插入，插入新节点并且返回根节点。

- 如果插入位置为空（初始为根节点），构造节点并插入到此位置， 返回此节点（根节点）。
- 若不为空，则与插入位置节点的key进行比较，若小于，则以此节点的左子节点node.left作为新的插入位置；若大于，则以此节点的右子节点node.right作为新的插入位置。
- 在新的插入位置递归的执行1-2步操作，并返回插入的节点（即以该位置为根的子树的根节点）。

##### 递归实现

```python
def _bst_insert_recursive(self, subtree, key, value):
    if subtree is None:
        subtree = BSTNode(key, value)
    elif key < subtree.key:
        subtree.left = self._bst_insert_recursive(subtree.left, key, value)
    elif key > subtree.key:
        subtree.right = self._bst_insert_recursive(subtree.right, key, value)
    return subtree
```

##### 非递归实现

- 如果二叉树为空，直接创建根节点。
- 否则循环的搜索新节点的插入位置（直到插入节点后返回函数），通过比较key值沿子节点关系向下：
  - 遇到应该走左子树而左子树为空，或者应该走向右子树而右子树为空时，即为新节点的插入位置，构造节点并插入到为空的子树。
  - 遇到key相等的节点，直接替换节点中的value并结束。

```python
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
```

### 删除节点

删除操作首先需要定位要删除的节点，其次在删除节点后要保持BST的性质。对于要删除的节点需考虑以下三种情况：

- 节点是叶节点没有孩子
- 节点有一个孩子
- 节点有两个孩子

#### 删除叶节点

只需要把它的父亲指向它的指针设置为 None 即可。

#### 删除只有一个孩子的节点

把它的父亲指向它的孩子即可。

#### 删除有两个孩子的内部节点

- 找到待删除节点的后继节点（中序遍历中的下一个值，右子树的最小值节点）
- 复制后继节点的key和value到待删除节点
- 从待删除节点的右子树中**递归地**删除后继节点

#### 代码实现

```python
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
```

### 时间复杂度分析

![img](assets/bst_worstcase.png)

平均来说时间复杂度和树的高度成正比为log(n)（**维持平衡二叉树的情况下**）， 但最坏情况下以上操作的时间复杂度都是 O(n)（树的结构退化）。

### 平衡二叉树

![../_images/bfderive.png](assets/bfderive.png)

#### 平衡二叉树定义

定义：是一类特殊的二叉查找树，它或为空树， 或者其左右子树都是平衡二叉树（是递归结构），而且其左右子树的高度之差的绝对值不超过1。

平衡因子**balance factor**：该节点的左子树的高度与右子树的高度之差。

如果能维持平衡二叉树的结构，查找操作就能在O(logn)时间内完成。

#### ADT实现

插入/删除操作的实现：首先根据key确定位置，实际插入或删除节点。如果这时出现树失衡的情况，设法进行局部调整回复树的平衡。插入和删除操作后的调整都可以在树中的一条路径上一遍完成，因此插入和删除操作的时间代价为O(logn)。

节点：实现AVL树，二叉树的每个节点需要增加一个平衡因子记录。

其余属性和插入删除以外的方法都可以从二叉查找树类中继承。

##### 插入后的失衡调整

1. LL失衡和调整

   ```python
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
   ```

2. RR失衡和调整

   ```python
   @staticmethod
   def RR(a, b):
       a.right = b.left
       b.left = a
       a.bf = b.bf = 0
       return b
   ```

3. LR失衡和调整

   ```python
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
   ```

4. RL失衡和调整

   ```python
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
   ```

##### 插入操作的实现

首先找到插入位置并实际插入新节点，然后可能需要修改一些节点的平衡因子，发现失衡时做一些局部调整（只需在最小不平衡子树的根节点附近左局部调整，不会影响其他部分，也不会改变树中数据的排序序列）

具体步骤：

- 查找新节点的插入位置，并在查找过程中记录遇到的最小不平衡子树的根，插入新节点。
- 修改从a的子节点到新节点的路径上各节点的平衡因子。
- 检查以a为根的子树是否失衡，失衡时做调整。
- 连接好调整后的子树，它可能该作为整棵树的根，或作为a原来的父节点的相应方向的子节点。（左或右节点）

代码实现：

```python
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
```

### B 树与B+ 树

#### B 树

![img](assets/8394323_13074405906V6Q.jpg)

下面，拟下查找文件29的过程：

1. 根据根结点指针找到文件目录的根磁盘块1，将其中的信息导入内存。【磁盘IO操作 1次】    
2. 此时内存中有两个文件名17、35和三个存储其他磁盘页面地址的数据。根据算法我们发现：17<29<35，因此我们找到指针p2。
3. 根据p2指针，我们定位到磁盘块3，并将其中的信息导入内存。【磁盘IO操作 2次】    
4. 此时内存中有两个文件名26，30和三个存储其他磁盘页面地址的数据。根据算法我们发现：26<29<30，因此我们找到指针p2。
5. 根据p2指针，我们定位到磁盘块8，并将其中的信息导入内存。【磁盘IO操作 3次】    
6. 此时内存中有两个文件名28，29。根据算法我们查找到文件名29，并定位了该文件内存的磁盘地址。

分析上面的过程，发现需要3次磁盘IO操作和3次内存查找操作。关于内存中的文件名查找，由于是一个有序表结构，可以利用二分查找提高效率。至于IO操作是影响整个B树查找效率的决定因素。

#### B+树

![img](assets/8394323_1307440587b6WG.jpg)

B+树是一种与B树类似的结构，但概念和实现稍微简单一些，同样采用节点分裂和合并的技术控制树高。B+树有以下性质：

- key在节点里排序存放。分支节点里的每一个key关联着一颗子树，这个key等于其所关联子树的根节点里的最大key。
- 叶节点里的每个key都关联着一个数据项的存储位置，数据项另行存储。（与B树不同，分支节点的key不关联数据项，只有叶节点的key关联数据项）
- 不同叶节点间顺序顺序的首尾链接，以方便顺序遍历。

相比B树有以下特点：

- B+**树的层级更少**：相较于B树B+每个**非叶子**节点存储的关键字数更多，树的层级更少所以查询数据更快；
- B+**树查询速度更稳定**：B+所有关键字数据地址都存在**叶子**节点上，所以每次查找的次数都相同所以查询速度要比B树更稳定;
- B+**树天然具备排序功能：**B+树所有的**叶子**节点数据构成了一个有序链表，在查询大小区间的数据时候更方便，数据紧密性很高，缓存的命中率也会比B树高。
- B+**树全节点遍历更快：**B+树遍历整棵树只需要遍历所有的**叶子**节点即可，，而不需要像B树一样需要对每一层进行遍历，这有利于数据库做全表扫描。

**B树**相对于**B+树**的优点是，如果经常访问的数据离根节点很近，而**B树**的**非叶子**节点本身存有关键字其数据的地址，所以这种数据检索的时候会要比**B+树**快。

### 红黑树

![img](assets/251730074203156.jpg)

#### 红黑树特性

1. 节点是红色或黑色。
2. 根是黑色。
3. 所有叶子节点都是黑色（叶子节点是NIL节点）。
4. 每个红色节点必须有两个黑色的子节点。（从每个叶子到根的所有路径上不能有两个连续的红色节点。）
5. 从任一节点到其每个叶子的所有简单路径都包含相同数目的黑色节点（简称黑高）。

通过以上性质作为约束，即可保证任意节点到其每个叶子节点路径最长不会超过最短路径的2倍。不严格控制左、右子树高度或节点数之差小于等于1，不用严格控制高度，使得插入效率更高。

插入和删除操作时，通过**变色**和**旋转**进行平衡调整。

红黑树高度依然是平均log(n)，且最坏情况高度不会超过2log(n)

#### 红黑树与AVL树的比较

1.查找

显然，AVL树要比红黑树更平衡，因此AVL树的查找效率更高。

2.插入和删除

红黑树的插入和删除都可以保证树的结构变化在常数范围，不用旋转调整至根节点，旋转次数更少，相对来说效率更高一些。

## 18 图与图的遍历

### 有向图的表示

![../_images/digraph.png](assets/digraph.png)

#### 邻接矩阵

![../_images/adjMat.png](assets/adjMat-1553007345454.png)

对于 n 个点，构造一个 n * n 的矩阵，如果有从点 i 到点 j 的边，就将矩阵的位置 matrix[i][j] 置为 1或权重值。适合在边的数量非常大时存储图。

优点：简单易理解，很容易找到邻接的顶点。

缺点：存储稀疏数据时空间利用效率低。

#### 邻接表

![../_images/adjlist.png](assets/adjlist.png)

将图中的点放到一个线性表中，对于每一个点将它的邻居放到一个链接到点对象本身的链表里。

图中用字典代替了链表。存放点对象的线性表也使用字典实现。

用邻接表可以紧凑的表示稀疏数据，同时很容易的找到所有与特定顶点直接相连的点。

### 使用邻接表实现图的ADT

创建 `Graph` 类表示存放顶点的主表，创建 `Vertex` 类表示图中的每个顶点。

#### 实现 Vertex 类

每个Vertex对象使用一个字典 `connectedTo`来保存与之连接的其他节点（名称），以及每条边的权重。

在类的构造方法中，直接初始化id（key字符串）以及邻接字典。

 `addNeighbor` 方法用来向顶点添加一个邻接的顶点。
 `getConnections` 方法返回顶点的邻接字典中的所有对象（通过 `connectedTo`来表示）
 `getWeight` 返回本顶点与作为参数传入的另一顶点之间边的权重值。

代码实现：

```python
class Vertex:
    def __init__(self, key):
        """
        在类的构造方法中，直接初始化id（key字符串）以及邻接字典。
        """
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        """
        添加邻接顶点，将邻接顶点对象以及相连边的权重作为参数传入
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        返回顶点的所有邻接顶点（的key），注意此返回结果为生成器
        """
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWight(self, nbr):
        """
        通过邻接顶点对象在邻接字典中获取权重值
        """
        return self.connectedTo[nbr]
```

#### 实现Graph类

`Graph` 类包含一个字典用来映射顶点名称与顶点对象，还提供了添加顶点以及连接两个顶点的方法。在构造方法中初始化字典以及表示顶点个数的属性。

 `getVertices` 方法返回字典中所有顶点的名称。 `__iter__` 方法遍历字典中的所有顶点对象。

```python
class Graph:
    def __init__(self):
        """
        在构造方法中初始化字典以及表示顶点个数的属性。
        """
        self.vertList = {}
        self.numVertics = 0

    def addVertex(self, key):
        """
        构造并添加顶点到图中
        """
        self.numVertics += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        """
        通过顶点key获取顶点对象，不存在返回None
        """
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, start, end, wight=0):
        """
        添加从start顶点到end顶点的边并设置权重，若顶点在图中不存在则创建顶点并加入图中
        """
        if start not in self.vertList:
            nv = self.addVertex(start)
        if end not in self.vertList:
            nv = self.addVertex(end)
        self.vertList[start].addNeighbor(self.vertList[end], wight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
```

### 图的遍历

#### BFS 广度优先搜索

在无权图中搜索两点之间的最短路径（即途径的边数最少）。

算法思路：

1. 构建队列，从将第一个节点的key放入队列，创建一个空集合用来保存访问过的节点。
2. 从队列中 pop 节点，检查节点是否在集合中。
3. 如果节点不在集合中，访问该节点并将其加入到已访问集合中，并依次将该节点的邻居节点 push 入队列。
4. 重复第2-3步，直到队列为空。

代码实现：

```python
def BFS(graph, start):
    search_queue = Queue()  # 用内置deque构建Queue
    searched = set()
    search_queue.push(start)
    while search_queue:
        cur_node = search_queue.pop()
        if cur_node not in searched:
            print(cur_node)  # or yield cur_node
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.push(node)
```

#### DFS 深度优先搜索

每遇到一个节点，如果没有被访问过，就直接去访问它的邻居节点，不断加深。

递归实现：

```python
DFS_searched = set()


def DFS_recursive(graph, start):
    if start not in DFS_searched:
        print(start)
        DFS_searched.add(start)
    for node in graph[start]:
        if node not in DFS_searched:
            DFS_recursive(graph, node)
```

堆栈实现（思路类似使用队列实现BFS）：

```python
def DFS(graph, start):
    s = Stack()
    s.push(start)
    searched = set()
    while not s.is_empty():
        cur_node = s.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in reversed(graph[cur_node]):
                s.push(node)
```

**对于不连通的图如何实现DFS：**对所有的顶点调用DFS()，并在调用前检查未被搜索过才执行。

### 拓扑排序

定义：将**有向无环图**(DAG)中的顶点以线性方式进行排序。对于任何连接自顶点**u**到顶点**v**的有向边**uv**，在最后的排序结果中，顶点**u**总是在顶点**v**的前面。

一个图的拓扑排序可以看成是图中所有顶点沿水平线排列而成的一个序列，使得所有的有向边均从左指向右。拓扑排序不同于通常意义上的排序。

#### 实际问题

拓扑排序通常用来“排序”具有依赖关系的任务。

比如，如果用一个DAG图来表示一个工程，其中每个顶点表示工程中的一个任务，用有向边 表示在做任务 B 之前必须先完成任务 A。故在这个工程中，任意两个任务要么具有确定的先后关系，要么是没有关系，绝对不存在互相矛盾的关系（即环路）。

#### 算法思想

借助深度优先遍历来实现拓扑排序。这个时候需要使用到栈结构来记录拓扑排序的结果。

执行过程中需考虑图中含有不连通的顶点，因此应尝试对所有顶点执行深度优先遍历（但在执行前检查是否已被搜索过）。

```js
L ← Empty list that will contain the sorted nodes
S ← Set of all nodes with no outgoing edges
for each node n in S do
    visit(n) 
function visit(node n)
    if n has not been visited yet then
        mark n as visited
        for each node m with an edgefrom m to ndo
            visit(m)
        add n to L
```

时间复杂度同DFS一致，为O(E+V)。

#### 代码实现

```python
s = Stack()
searched = set()
for node in graph: # 考虑图中含有不连通的顶点
    topologicalSort(graph, node)
def topologicalSort(graph, start):
    if start not in searched:
        searched.add(start)
    for node in graph[start]:
        if node not in searched:
            DFS_recursive(graph, node)
        s.push(node)
```

添加顶点到堆栈中的时机是在**dfs**方法即将退出之时，而**dfs**方法本身是个递归方法，只要当前顶点还存在边指向其它任何顶点，它就会递归调用**dfs**方法，而不会退出。因此，退出**dfs**方法，意味着当前顶点没有指向其它顶点的边了，即当前顶点是一条路径上的最后一个顶点。

最后逐个弹出堆栈的中顶点，即得到线性排序结果。

### 最短路径问题与 Dijkstra 算法

#### 单源最短路径

![../_images/routeGraph.png](assets/routeGraph.png)

现实问题：在网络的不同路由节点中，寻找传输最快的路径。

抽象为在图中寻找权重值weight之和最小的路径，当所有边的权重值相等即图为无权图时，应使用广度优先搜索最近的顶点。

#### Dijkstra 算法

“Dijkstra”算法是一种迭代算法，用来提供从一个确定的开始节点到所有图中其他节点的最短路径，这与广度优先搜索的结果很类似。

关键理念是找出图中最便宜的节点，并确保没有到该节点的更便宜的路径。

##### 适用范围

~~迪克斯特拉算法只适用于有向无环图。~~加权的有向图和无向图都可以使用迪克斯特拉算法。

但如果有负权边，不能使用迪克斯特拉算法。

##### 主要思路

1. 找出最便宜的节点，即可在最短时间内前往的节点。
2. 对于该节点的邻居，检查是否有前往它们的更短路径，如果有，更新其开销。
3. 重复这个过程，直到对图中的每个节点都这样做了。
4. 计算最终路径。

##### 基础理解

找到最便宜的节点：

1. 首先将最小开销设为无穷大，将最小开销节点设为None。
2. 遍历开销表中的所有节点，如果该节点未被处理过且开销小于最小开销，就将其视为开销最低的节点，从而找出开销表未被处理的节点中开销最小的节点。
3. 返回开销最小的节点。

算法所需数据结构：

- 使用一个散列表保存所有节点以及邻居节点。
- 使用一个散列表保存每个节点的开销，即从起点出发到该节点的权重值之和，初始为无限大。
- 使用一个散列表保存每个节点的父节点。
- 使用一个集合来记录处理过的节点，每个节点只需处理一次。

##### 进阶理解

- 将图中所有顶点分为两个集合，一个为已确定最短路径的顶点集合U（初始为出发顶点），一个为未确定最短路径的顶点集合S（与出发顶点有直接边相连的最短路径为相连边的权重值，其余顶点的最短路径设为无穷大）
- 从S中取出在集合中当前最短路径长度最小的顶点，求出其邻居节点的最短路径（当前节点最短路径+相邻边的权重值），若该最短路径小于邻居节点当前的最短路径，则在集合S中进行更新。
- 将此节点加入集合U中，集合U的节点的最短路径长度必为最终的最短路径（即最短），因此不会再被更新。继续从集合S中取出节点重复此步骤，直到所有顶点都包含在集合U中。

考虑的因素：节点**Node**，是否已确认最短路径**Known**，最短路径长度**Cost**（确认后不再变化），父节点**Parent**（用来计算最终路径）

使用最小堆实现优先级队列来保存未确定最短路径的顶点。

##### 简单实现

使用快排或遍历等方法获取未确定最短路径顶点中当前距离最小的顶点。

```python
nodes = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

unvisted = {node:float('inf') for node in nodes}
visted = {}
current = 'B'
currentDistance = 0
unvisted[current] = currentDistance

while True:
    for neighbor, distance in nodes[current].items():
        if neighbor not in unvisted:
            continue
        newDistance = currentDistance + distance
        if newDistance < unvisted[neighbor]:
            unvisted[neighbor] = newDistance
    visted[current] = currentDistance
    del unvisted[current]
    if not unvisted:
        break
    candidates = [node for node in unvisted.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visted)
```

时间复杂度为O(n^2^)。

##### 进阶实现

使用优先级队列作为未确定最短距离顶点的集合，以降低算法的时间复杂度。

```python
def dijkstra(graph, start):
    # 用图中的节点构建优先级队列
    pq = PriorityQueue()
    start.setDistance(0)
    pq_list = [(v, v.getDistance()) for v in graph]
    for v, priority in pq_list:
        pq.add_task(v, priority)
    # 从队列中取出路径长度最小的顶点，更新其邻居节点的距离
    while not pq.is_empty():
        currentVert = pq.pop_task()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.add_task(nextVert, newDist)  # 通过此方法更新队列中任务的优先级

```

需要额外实现的方法：`pq.add_task()`更新队列中已有任务的优先级。我们使用的实现是将现有任务标记为REMOVED然后添加一个修改过优先级的新任务。

时间复杂度为O(n*logn)，准确的说为O((V+E)log(V))，V为顶点个数，E为边的个数.

### 最小生成树问题与 Prim 算法

#### 最小生成树

给定一个相连的正加权图G，找到连接所有顶点且权重值之和最小的边的集合。

该问题是很多应用的基础问题：如电话、通信以及交通网络的设计，连接所有节点且损耗最小。

#### Prim 算法

属于贪心算法的一种。

##### 算法思想

开始假设有一个空的生成树，将图中所有顶点分为两个集合，一个包含已经在最小生成树MST中的顶点，一个包含未在最小生成树中的顶点。在每一步，考虑连接以上两个集合（即连接的顶点分别属于不同集合）的所有边，并从中选出权重值最小的边，然后将边的另一端点，即未在最小生成树中的顶点，加入到包含最小生成树的集合。

背后的思想：一个生成树意味着所有顶点都会相连，所以上述的两个集合中的顶点必须相连才能构成生成树，而且它们必须通过权重值最小的边相连，才能使生成树称为最小生成树。

##### 步骤

1. 创建一个集合mstSet记录已经在最小生成树中的顶点。
2. 对输入的图中的所有顶点赋予一个关键值key，key的初始值为无穷大（float('inf')），将起始顶点的key值设为0.
3. 当前最小生成树没有包含所有顶点时：
   - 选出一个没在mstSet中且拥有最小key值的顶点 u。
   - 将 u 加入mstSet。
   - 更新 u  的所有邻接节点的key值。对于每一个邻接顶点 v ，如果相邻边 u-v 的权重值小于v 原来的key值，则将key值更新为 u-v 的权重值。

#### 代码实现

类似于Dijkstra算法。

```python
def prim(graph, start):
    # 构造优先级队列
    pq = PriorityQueue()
    start.setDistance(0)
    pq_list = [(v, v.getDistance()) for v in graph]
    for v, priority in pq_list:
        pq.add_task(v, priority)
    # 从队列中取出当前距离最小的顶点，更新其邻居节点的距离
    while not pq.is_empty():
        currentVert = pq.pop_task()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getWeight(nextVert)
            if nextVert in pq and newDist < nextVert.getDistance():
                # 更新队列中节点的距离和父节点
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.add_task(nextVert, newDist)
```

## 19 Python 常用内置算法和数据结构

| 数据结构/算法 | 语言内置                        | 内置库                                                       |
| ------------- | ------------------------------- | ------------------------------------------------------------ |
| 线性结构      | list(列表)/tuple(元祖)          | array(数组，不常用)/collections.namedtuple                   |
| 链式结构      |                                 | collections.deque(双端队列)                                  |
| 字典结构      | dict(字典)                      | collections.Counter(计数器)/OrderedDict(有序字典)/defaultdict |
| 集合结构      | set(集合)/frozenset(不可变集合) |                                                              |
| 排序算法      | sorted                          |                                                              |
| 二分算法      |                                 | bisect模块                                                   |
| 堆算法        |                                 | heapq模块（最小堆）                                          |
| 缓存算法      |                                 | functools.lru_cache(Least Recent Used, python3)              |

## 20 参考

- [Python 算法与数据结构视频教程](<https://python-data-structures-and-algorithms.readthedocs.io/zh/latest/>)
- [Problem Solving with Algorithms and Data Structures using Python](<http://interactivepython.org/runestone/static/pythonds/index.html#problem-solving-with-algorithms-and-data-structures-using-python>)
- [Graph Data Structure And Algorithms](<https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/>)
- [算法图解](<https://book.douban.com/subject/26979890/>)
- [数据结构与算法：Python语言描述](<https://book.douban.com/subject/26702568/>)
