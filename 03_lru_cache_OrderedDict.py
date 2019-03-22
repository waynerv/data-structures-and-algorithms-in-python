"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除删除最长时间未使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""

from collections import OrderedDict


class LRUCache(object):
    """Implement LRUCache using OrderedDict"""

    def __init__(self, capacity: int):
        self._ordered_dict = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:  # 取回值，假定值存在，若不存在返回-1
        self._move_to_end_if_exist(key)

        return self._ordered_dict.get(key, -1)

    def put(self, key: int, value: int) -> None:  # 添加或更新键值对
        self._move_to_end_if_exist(key)

        self._ordered_dict[key] = value
        if len(self._ordered_dict) > self._capacity:
            self._ordered_dict.popitem(last=False)  # popitem支持弹出头部或尾部

    def _move_to_end_if_exist(self, key: int) -> None:
        if key in self._ordered_dict:
            self._ordered_dict.move_to_end(key)
