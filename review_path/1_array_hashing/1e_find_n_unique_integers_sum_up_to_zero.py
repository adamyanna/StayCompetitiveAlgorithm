#!/usr/bin/env python3

# Find N Unique Integers Sum up to Zero
#  和为零的N 个不同整数(给你一个整数 n ，请你返回n 个整数的数组，和为零)
# range n // 2 各取一半正负数
# n为even 直接返回
# n为odd append 0

class Solution(object):
    def sumZero(self, n):
        result = []
        for i in range(0, (n // 2) +1):
            result.append(i)
            result.append(-i)
        if n % 2 > 0:
            # odd
            result.append(0)
        return result