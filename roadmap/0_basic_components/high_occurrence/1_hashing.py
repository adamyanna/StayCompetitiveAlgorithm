#!/usr/bin/env python3

"""
Using Array & Linked List to Implement a Hash Table
"""
class Link(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
class HashTablePractice(object):
    def __init__(self, length):
        """
        Using list or string to implement a time O(1) hash table
        """
        self.initial_len = length
        self.store = [None] * self.initial_len
        self.size = 0

    def get_key_index(self, k):
        order = 0
        for v in str(k):
            order += ord(v)
        return order % self.initial_len

    def get_key_node(self, k):
        index = self.get_key_index(k)
        if self.store[index]:
            link = self.store[index]
            while link:
                if link.key == k:
                    return link
                link = link.next
        return None

    def put(self, k, v):
        exist_link = self.get_key_node(k)
        if exist_link:
            if v != exist_link.val:
                exist_link.val = v
            return
        index = self.get_key_index(k)
        if self.store[index] is None:
            self.store[index] = Link(k, v)
        else:
            self.store[index].next = Link(k, v)
        self.size += 1

    def get(self, k):
        exist_link = self.get_key_node(k)
        if exist_link:
            return exist_link.val
        return None

    def get_size(self):
        return self.size

    def empty(self):
        return True if self.size == 0 else False


class DLinkedList(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        self.cache = dict()

        self.head = DLinkedList(None, None)
        self.tail = DLinkedList(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.size = 0

    def remove_last(self):
        # tail.prev.prev - tail.prev - tail
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

    def move_node_to_head(self, node):
        # remove node
        node.next.prev = node.prev
        node.prev.next = node.next
        # add node to begin
        # head - node - head.next
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def put(self, k, v):
        if k not in self.cache:
            node = DLinkedList(k, v)
            self.cache[k] = node
            # add to the link list
            # head - node - head.next
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.size += 1
            # remove last used element
            if self.size > self.capacity:
                # remove from hashmap
                self.cache.pop(self.tail.prev.key)
                # remove tail.prev
                self.remove_last()
                self.size -= 1
        else:
            # k existed & key used
            node = self.cache[k]
            node.val = v
            # move node to front
            self.move_node_to_head(node)

    def get(self, k):
        if k in self.cache:
            # update lru
            node = self.cache[k]
            # move node to front
            self.move_node_to_head(node)
            # return
            return node.val
        else:
            return None


if __name__ == '__main__':

    lru = LRUCache(3)
    lru.put(1,1)
    lru.put(2,2)
    lru.put(3,3)
    print(lru.get(1))
    print(lru.get(2))
    lru.put(4,4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
    print(lru.get(1))


    # h = HashTablePractice(1000)
    # print(h.empty())
    # h.put("schedule", "19:07")
    # print(h.get("schedule"))
    # h.put(1, 999)
    # print(h.get_size())
    # h.put("schedule", "11:00")
    # print(h.empty())
    # print(h.get_size())
    # print(h.get("schedule"))

