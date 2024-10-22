#!/usr/bin/env python3

# Add Two Numbers II
"""
* 两数相加 II 链表-(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4) 输出: 7 -> 8 -> 0 -> 7 高位在左
* 1. 通过while 循环找到长链表为1，短链表为2，i1，i2，分别为末尾下标
* 2. 通过实现 add method，将长链表和短链表以递归形式相加，递归的本质就是回溯到0 index开始往上相加，
    如果值对于10（十进制）取模就十当前index 下的值，并且递归的return需要决定next是否需要进位（也就是加1），可以直接返回 // 相除的结果
* 3. 递归的条件，应该就是，对于长度相同的位置和不同的位置，有两种不同的处理方式
    1. 相同的位置就应该是 两个位置相加 + 递归返回的进位值
    2. 不同的值的处理方式就是应该是 当前位置的值 + 递归返回值（是否要进位），每次递归都应该将长链表的长度 - 1，以达成相同长度时候的条件
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """

    # 分析
    # 通过两个while循环找到当前最长的那个链表，长串long、短串short，处理边界
    # 递归：
    #   - 两种情况：长串大于短串的部分：

    def addNum(self, long_num, short_num, long_link, short_link):

        if long_num > short_num:
            # 对于长出的部分，只需要增加可能会出现的进位即可
            # 递归属于回溯的方式，每一次调用的返回值都可以往前回溯，第一次返回即链表尾部
            t_value = long_link.val + self.addNum(long_num - 1, short_num, long_link.next, short_link)
        else:
            # 长度相同的部分，需要值相加并进位
            t_value = long_link.val + short_link.val + self.addNum(long_num - 1, short_num - 1, long_link.next,
                                                              short_link.next)
        # 十进制低位结果
        low = t_value % 10
        # 十进制高位结果
        high = t_value // 10
        # 更新当前node值
        long_link.val = low
        # 返回进位
        return high

    def addTwoNumbers(self, l1, l2):
        def add(num1, num2, i, j):
            if not i or not j:
                return 0
            # nums1为长串，在长串本身上进行修改，temp值为该点值加进位值，递归调用i.next
            if num1 > num2:
                temp = i.val + add(num1 - 1, num2, i.next, j)
            else:
                # 递归调用直到两个长度相等，继续递归相同长度的两个链表，
                # 当i next和j next到达末尾时，第一次返回，相加并修改i的值为tmp%10，返回进位值1或者0
                # 前一个相加会继续更新，直到返回到num1》num2的位置
                temp = i.val + j.val + add(num1, num2, i.next, j.next)
            i.val = temp % 10
            return temp // 10

        num1 = num2 = 0
        cur = l2
        while cur:
            num2 += 1
            cur = cur.next
        cur = l1
        while cur:
            num1 += 1
            cur = cur.next

        if num2 > num1:
            l1, l2 = l2, l1
            num2, num1 = num1, num2

        if add(num1, num2, l1, l2):
            l2 = ListNode(1)
            l2.next = l1
            l1 = l2
        return l1
