#!/usr/bin/env python3

# Two Sum
# 一次遍历
# 保存 hash，检查是否存在 target - value，返回i 和 hash[target - value]
# O(N)

"""
solution point: target - x, will only need to get from current map itself,
for future element it will find it's pair back to map
"""


class Solution(object):
    def twoSum(self, nums, target):
        t_map = {}
        for i in range(0, len(nums)):
            if target - nums[i] in t_map:
                return [t_map[target - nums[i]], i]
            t_map[nums[i]] = i
        return []
