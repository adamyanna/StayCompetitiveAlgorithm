#!/usr/bin/env python3

"""
reverse-nodes-in-k-group

输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

只用 O(1) 额外内存空间
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

class Solution(object):
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        if not head: return head

        self.did_reverse = True
        def reverse_recur(node, i):
            if i < k and not node:
                self.did_reverse = False
            if i == k:
                return node
            n_node = reverse_recur(node.next, i+1)
            if self.did_reverse: n_node.next = node
            return node

        result_head = None
        last_tail = None

        while head:
            index = 0
            new_head = head
            for i in range(1, k):
                if new_head.next:
                    new_head = new_head.next
                    index = i
                else:
                    break
            if index < k-1:
                # list nodes count < k, no need to reverse
                break
            if not result_head: result_head = new_head
            new_head_n = new_head.next

            current_tail = reverse_recur(head, 1)
            current_tail.next = new_head_n
            if last_tail:
                last_tail.next = new_head
            last_tail = current_tail
            head = new_head_n

        return result_head if result_head else head

if __name__ == '__main__':
    link = deserialize_array_to_linked_list([1,2,3,4,5,6,8])
    swap_link = Solution().reverse_k_group(link, 10)
    result = []
    while swap_link:
        result.append(swap_link.val)
        swap_link = swap_link.next
    print(result)