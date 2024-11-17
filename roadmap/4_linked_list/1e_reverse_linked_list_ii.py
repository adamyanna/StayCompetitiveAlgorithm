#!/usr/bin/env python3

"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
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
    def reverse_linked_list(self, head, left, right):
        """
        输入：head = [1,2,3,4,5], left = 2, right = 4
        输出：[1,4,3,2,5]
        :param head:
        :return:
        """
        if not head: return
        result = head
        index = 0
        last = None
        before_left = None
        at_left = None
        while head:
            index += 1
            if index < left:
                before_left = head
                head = head.next
            elif left <= index <= right:
                if last is None:
                    at_left = head
                # if not last:
                #     at_left = head
                # 1 - 2 - 3
                tmp = head.next
                head.next = last
                last = head
                head = tmp
            else:
                at_left.next = head
                break
        if before_left:
            before_left.next = last

        return last if not before_left else result




if __name__ == '__main__':
    root = deserialize_array_to_link_list([1,2,3,4,5,6])
    n_root = Solution().reverse_linked_list(root, 2, 4)
    while n_root:
        print(n_root.val)
        n_root = n_root.next

