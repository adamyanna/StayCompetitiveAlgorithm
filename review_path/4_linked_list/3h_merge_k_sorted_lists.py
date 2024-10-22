#!/usr/bin/env python3

# Merge k Sorted Lists
"""* 合并K个排序链表
* 基于两个链表合并的算法，我们将k中每两个链表合并一次得出的新的集合再进行同样的操作，
    最终得到一个集合，T = kN 将 k 个链表配对并将同一对中的链表合并。第一轮合并以后，
    k 个链表被合并成了 k/2 个链表，平均长度为 2N/k 重复这一过程，直到我们得到了最终的有序链表。
    每次k的数目指数型下降，例如k k/2 k/4 k/8 S = Nlogk
* 合并两个升序链表的方法：
    - 考虑几种情况，1. 逐个更新并对比插入 2. 不存在插入的情况，直接插入到链表尾部
    - 选取首个 node 值小的 node 作为被插入链表 head，另一个首个 node 大的为 tail
    - 在找到可以将 tail 首个 node 插入 head 和 head.next 之间之前，不断更新 head
    - 两次循环分别为 while head: while head.next.val >= tail.val:
    - 存在的三种边界情况，head 循环后为None，tail 循环后为None，head.next 循环后为None
* k个链表的处理方法：
    - 从结果数组两端开始 merge
    - 初始化一个新的 merge 数组，从0和-1开始，从list两端的链表开始merge
    - while list // 2 > 0 的情况下，循环 merge
    - 并且每次merge结束后，将两端的结果 pop 去除出原始的 list，list的长度就会减小，直到为空或者剩下一个链表
    - 更新新的 merge 到起始的merge，直到起始merge长度小于0，即退出循环
"""

#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 合并K个排序链表
        # 基于两个链表合并的算法，我们将k中每两个链表合并一次得出的新的集合再进行同样的操作，最终得到一个集合，
        # T = kN 将 k 个链表配对并将同一对中的链表合并。
        # 第一轮合并以后， k 个链表被合并成了 k/2 个链表，平均长度为 2N/k
        # 重复这一过程，直到我们得到了最终的有序链表。
        # 每次k的数目指数型下降，例如k k/2 k/4 k/8 S = Nlogk

        # 边界条件
        if not lists:
            return None
        # 初始化一个结果tuple合集，左值为链表首个node值，右值为链表
        # 使用 python lambda 函数对list做一次基于 lamdba k: k[0] 的排序
        l_merge = []
        for l in lists:
            if l:
                l_merge.append((l.val, l))
        if not l_merge:
            return None
        l_merge = sorted(l_merge, key=lambda k: k[0])


        print(l_merge)

        # 从结果数组两端开始 merge
        # 初始化一个新的 merge 数组，从0和-1开始，从list两端的链表开始merge
        # while list // 2 > 0 的情况下，循环 merge
        # 并且每次merge结束后，将两端的结果 pop 去除出原始的 list，list的长度就会减小，直到为空或者剩下一个链表
        # 更新新的 merge 到起始的merge，直到起始merge长度小于0，即退出循环
        while len(l_merge) > 1:
            i = 0
            new_l_merge = []
            while i < len(l_merge) / 2:
                new_l = self.mergeTwoLists(l_merge[i][1], l_merge[len(l_merge) - 1 -i][1])
                l_merge.pop(i)
                l_merge.pop(len(l_merge) - 1 -i)
                new_l_merge.append((new_l.val, new_l))
            if l_merge:
                new_l_merge.extend(l_merge)
            l_merge = new_l_merge
        return l_merge[0][1]

    # already analyzed
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        else:
            pass

        if l1.val < l2.val:
            head = l1
            tail = l2
        else:
            head = l2
            tail = l1
        result = head
        while head:
            if not head or not tail:
                break
            if not head.next and tail:
                head.next = tail
                break
            while head.next.val >= tail.val:
                tmp = ListNode(tail.val)
                tmp.next = head.next
                head.next = tmp
                tail = tail.next
                if not tail and head:
                    break
            head = head.next
        return result
