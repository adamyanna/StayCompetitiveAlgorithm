#!/usr/bin/env python3

"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""

class LinkedList(object):
    def __init__(self, val, n=None):
        self.val = val
        self.next = n

def deserialize_array_to_link_list(array):
    if not array or not array[0]: return None

    head = LinkedList(array[0])
    result = head
    for i in range(1, len(array)):
        head.next = LinkedList(array[i])
        head = head.next
    return result


class Solution(object):
    def reverse_linked_list(self, head):
        """
        1 - 2 - 3 - 4
        :param head:
        :return:
        """
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp

        return last


if __name__ == '__main__':
    root = deserialize_array_to_link_list([1,2,3,4,5,6])
    n_root = Solution().reverse_linked_list(root)
    while n_root:
        print(n_root.val)
        n_root = n_root.next


