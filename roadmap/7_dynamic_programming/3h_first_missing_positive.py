#!/usr/bin/env python3

# First Missing Positive
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# 分析
# 目标是：最小的正整数，math上最小的正整数为1，那么答案就是从1开始递增到某一个数值
# 考虑极端情况，如果当前 nums 中 1~N 是，1~N以内所有的正整数分布，那么答案就是 N+1
# 那么就有，如果当前 nums 中任意x位置的数不是 1~N 之间，那么可以确定答案就在 1~N 之间
# 这样就可以利用0 ~ N-1个索引保存当前已经出现过的 1~N 之间正整数的存在状态
# 最终0 ~ N-1个索引中第一个未标记的索引 I，I+1 就是我们需要求得的结果
# 可以完全去除所有小于等于0的数的影响

"""
Tricky !!!
Use positive + & negative - & array index to store existed state of a positive integer
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 更新当前nums去除所有负值和0
        length = len(nums)
        nums = [length for n in nums if n <= 0]

        # 迭代当前nums，将所有的1~len(nums)之间的数字存储在nums index状态上
        for n in nums:
            # convert each number as array index & store existed state
            idx = abs(n) - 1
            if -1 < idx < len(nums):
                nums[idx] = -abs(nums[idx])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1