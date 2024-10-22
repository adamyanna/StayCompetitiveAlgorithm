# LRU Cache
"""
* OrderedDcit()
* 不用有序字典再次实现

# Another approch(do not use OrderDict build in type)

# 双向链表
# hash map
# 分析：双向链表 + hash
# 使用双向链表，定一个None值的tail和None值的head，并保存为实例变量，当前put的size大于容量，即可以直接找到tail.prev.key, 将其从 hash 中删除，hans中保存(key,dlinknode(key,v))
# 操作：
# 1. get -> 判断 key 是否在 hash 中否则返回-1，如果存在，则找到他值，并且还需要将他更新为最新访问的node，移动到 doublelink head
# 2. put -> key 不存在，创建新的node，更新 hash，判断容量，否则node移动到head，是则删除tail.prev，存在则直接更新v，并移动到head
"""

# 定义一个双向链表
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # 初始化一个 hash
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        # 定义一个head，一个tail并将其相连
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        # capacity 定义当前初始化的 size
        self.capacity = capacity
        # current size
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        # add a node to the head of a link
        # but after head
        # set node's next to head's next
        # set node's prev to head's prev
        # update prev of head's next to node
        # update head next to node
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        # remove a node
        # change node's prev next to node's next
        # change node's next prev to node's prev
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        # move a not to head
        # remove it & add to head again
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        # remove last used one
        # get from tail's prev
        # call remove
        node = self.tail.prev
        self.removeNode(node)
        return node



# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


# class LRUCache(OrderedDict):
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self:
#             return - 1
#
#         self.move_to_end(key)
#         return self[key]
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)
