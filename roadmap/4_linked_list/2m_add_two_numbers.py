#!/usr/bin/env python3

# Add Two Numbers / 非空链表两数相加&逆序
# - find long & use iteration add
"""
* 两数相加，逆序数字链表，相加得到新链表 (2 -> 4 -> 3) + (5 -> 6 -> 4) 输出：7 -> 0 -> 8
* 两个链表都存在且非空，一次while循环，考虑边界条件
* 初始化新的链表用于保存结果，任意一个链表next为None则跳出
* 初始化结果的下一个node
* 大于10需要进位，每次相加都要检查当前是否已存在1
* 每一次循环末尾都需要更新结果链表到下一位
"""


#
# [2] 两数相加
# 两数相加，逆序数字链表，相加得到新链表 (2 -> 4 -> 3) + (5 -> 6 -> 4) 输出：7 -> 0 -> 8

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    r = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 分析
        # 创建一个新的链表起点，起点val为0
        # 开始循环
        result = ListNode(0)
        Solution.r = result

        while True:
            # 1. 两个链表都存在且非空
            #       暂存当前node值之和为t，更新当前var为next
            if l1 and l2:
                t_sum = l1.val + l2.val

                l1 = l1.next
                l2 = l2.next
            # 其中一个链表为空
            #       暂存当前node值为t，更新当前var为next
            elif not l1 and l2:
                t_sum = l2.val
                l2 = l2.next
            elif not l2 and l1:
                t_sum = l1.val
                l1 = l1.next
            # 都空 t 为 0
            else:
                t_sum = 0

            # 初始化结果的下一个node
            Solution.r.next = ListNode(0)

            # 检查当前是否已经有前一次loop的进位，并更新t
            if Solution.r.val != 0:
                t_sum = t_sum + Solution.r.val

            # 十进制，大于10，则需要进位
            if t_sum >= 10:
                t_sum = t_sum - 10
                Solution.r.next.val = 1
            else:
                Solution.r.next.val = 0

            # 更新 t_sum
            Solution.r.val = t_sum

            # 任意一个链表当前的next值为 None，则已完成并跳出
            if not l1 and not l2:
                # 头部不能出现0值，需要设置为 None
                if Solution.r.next.val == 0:
                    Solution.r.next = None
                break

            # 每一次循环末尾都需要更新结果链表到下一位
            Solution.r = Solution.r.next

        print(result)

        return result
