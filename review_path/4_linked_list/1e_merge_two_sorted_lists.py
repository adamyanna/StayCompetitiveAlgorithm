#!/usr/bin/env python3

# 合并两个升序链表
# l1、l2 是两个升序链表，将其合并为一个升序链表并返回
# l1 = 1 -> 3 -> 7 -> 11
# l2 = 0 -> 2 -> 9 -> 10
# 分析
# 选取 l2 为 head，l1 作为 head
# [while head] 循环 while 找到第一个 head.next 比 tail 首个 node 大的 head.next，表示可以将 tail 插入 head.next 之前
# [while head.next.value >= tail.value]插入的情况为初始化新的node，将新的node插入到当前 head.next 之前 t.next = h.next h.next = t
# 完成插入后同时更新 tail，如果tail继续满足循环，则继续插入，否则跳出循环，并更新head
# 考虑边界条件

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # 边界条件处理
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        else:
            pass

        # 选定头部：
        # 比较两个链表首个node值的大小获取当前最小值作为输出链表的起始值
        if l1.val < l2.val:
            head = l1
            tail = l2
        else:
            head = l2
            tail = l1

        # 初始化一个结果，将当前head作为结果
        result = head
        while head:
            # 边界条件处理
            # head 或 tail 不存在结束循环
            if not head or not tail:
                break
            # head next不存在 且 tail 存在
            # 将 tail 赋值给 head.next 并退出循环
            if not head.next and tail:
                head.next = tail
                break
            # 当 head.next.val 大于或等于 tail.val
            # 暂存当前tail值，并初始化创建新的node
            # 将新的node插入到当前 head.next 之前 t.next = h.next h.next = t
            # 并更新tail 到 tail.next
            # 当 tail 为空 且 head 存在，则直接退出循环
            while head.next.val >= tail.val:
                tmp = ListNode(tail.val)
                tmp.next = head.next
                head.next = tmp
                tail = tail.next
                if not tail and head:
                    break
            # 更新 head 到 next
            head = head.next
        return result
