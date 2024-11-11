#!/usr/bin/env python3

"""
merge_k_sorted_lists

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deserialize_array_to_linked_list(array):
    if not array or not array[0]: return None
    import queue
    q = queue.Queue()
    head = ListNode(array[0])
    q.put(head)
    index = 1
    while index < len(array) and not q.empty():
        node = q.get()
        node.next = ListNode(array[index])
        q.put(node.next)
        index += 1
    return head


def serialize_linked_list_to_array(link):
    if not link: return []
    result = []
    while link:
        result.append(link.val)
        link = link.next
    return result


class CustomHeap(object):

    def __init__(self):
        self.heap = []
        self.size = 0

    def __adjust_helper(self, array, length, i):
        head = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < length and array[i] > array[left]:
            head = left
        if right < length and array[head] > array[right]:
            head = right
        if head != i:
            array[i], array[head] = array[head], array[i]
            self.__adjust_helper(array, length, head)
        return array

    def __construct_min_heap(self, unsorted_array):
        l = len(unsorted_array)
        for i in range(l, -1, -1):
            self.__adjust_helper(unsorted_array, l, i)

    def push(self, val):
        self.heap.insert(0, val)
        self.size += 1
        return self.__adjust_helper(self.heap, self.size, 0)

    def pop(self):
        val = self.heap.pop(0)
        self.size -= 1
        self.__construct_min_heap(self.heap)
        return val


class Solution(object):
    def merge_k_lists(self, lists: list[ListNode]):
        """
        Analyze
        1. add all linked list first elements into heap
        2. get first smallest, put into result
        3. add got list next into heap
        repeat until the empty heap
        :param lists:
        :return:
        """
        if not lists:
            return None
        import heapq
        sorted_h = []
        self.head = None
        self.result = None
        while True:
            for index in range(len(lists)):
                node = lists[index]
                if not node: continue
                heapq.heappush(sorted_h, (node.val, index))
                lists[index] = node.next

            if len(sorted_h) > 0:
                sorted_val, list_index = heapq.heappop(sorted_h)

                if self.head is None:
                    self.head = ListNode(sorted_val)
                    self.result = self.head
                else:
                    self.result.next = ListNode(sorted_val)
                    self.result = self.result.next
                if lists[list_index]:
                    heapq.heappush(sorted_h, (lists[list_index].val, list_index))
                    lists[list_index] = lists[list_index].next

            if not sorted_h:
                return self.head


if __name__ == '__main__':
    lists = [deserialize_array_to_linked_list([1, 4, 5]), deserialize_array_to_linked_list([1, 3, 4]),
             deserialize_array_to_linked_list([2, 6])]
    link = Solution().merge_k_lists(lists)
    print(serialize_linked_list_to_array(link))

    h = CustomHeap()
    h.push(9)
    h.push(5)
    h.push(8)
    h.push(1)
    h.push(10)
    # print heap
    level = 0
    count = 0
    level_result = []
    result = []
    h.pop()
    for i in range(len(h.heap)):
        level_result.append(h.heap[i])
        count += 1
        if count == 2**level:
            count = 0
            level += 1
            result.append(level_result[:])
            level_result = []
        if i == len(h.heap) - 1 and len(level_result) > 0:
            result.append(level_result)
    for v in result:
        print(v)


