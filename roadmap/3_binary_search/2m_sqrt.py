#!/usr/bin/env python3

# Sqrt
# x的平方根

# 利用二分查找的方式
# 定义L、R分别为0和输入值
# 利用二分法，取 L + R // 2
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = -1
        while l <= r:
            m = (l+r) // 2
            if m * m == x:
                result = m
                break
            elif m * m < x:
                # find 1st value m^2 less than x is result
                result = m
                # update left to increase the value
                l = m + 1
            else:
                # update r to decrease the value
                r = m - 1
        return result