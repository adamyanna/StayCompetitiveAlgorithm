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

if __name__ == '__main__':
    h = HashTablePractice(1000)
    print(h.empty())
    h.put("schedule", "19:07")
    print(h.get("schedule"))
    h.put(1, 999)
    print(h.get_size())
    h.put("schedule", "11:00")
    print(h.empty())
    print(h.get_size())
    print(h.get("schedule"))

