#!/usr/bin/env python3

"""
Tricky !!!
再每个递归中初始化一个 set，每一次递归都表示对first开始到数组结束进行全排列，每一个递归中都有可能出现重复
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 1224 生成set，set=1，1原地交换
        # 1224 1不变，生成set，set=2，2原地交换
        # 1224 12不变，生成set，set=2，2原地交换
        # 1224
        def backtrack(first=0):
            if first == n:
                result.append(nums[:])
            s = set()  # 再每个递归中初始化一个 set，每一次递归都表示对first开始到数组结束进行全排列，每一个递归中都有可能出现重复
            for i in range(first, n):
                if nums[i] in s: continue
                s.add(nums[i])
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        result = []
        backtrack()
        return result
