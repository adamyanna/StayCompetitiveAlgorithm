#!/usr/bin/env python3

"""
swap-nodes-in-pairs

输入：head = [1,2,3,4]
输出：[2,1,4,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deserialize_array_to_linked_list(array):
    import queue
    if not array or not array[0]: return None
    head = ListNode(array[0])
    index = 1
    q = queue.Queue()
    q.put(head)
    while index < len(array) and not q.empty():
        node = q.get()
        node.next = ListNode(array[index])
        q.put(node.next)
        index += 1

    return head

class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        """
        1 -> 2 -> 3 -> 4
        :param head:
        :return:
        """
        if not head: return None

        new_head = head.next

        previous = None

        while head and head.next:
            h_next = head.next
            head.next = h_next.next
            h_next.next = head
            if previous:
                previous.next = h_next
            previous = head
            head = head.next

        return head if not new_head else new_head


if __name__ == '__main__':
    link = deserialize_array_to_linked_list([1])
    swap_link = Solution().swap_pairs(link)
    result = []
    while swap_link:
        result.append(swap_link.val)
        swap_link = swap_link.next
    print(result)