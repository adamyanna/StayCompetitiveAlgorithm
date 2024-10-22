#!/usr/bin/env python3

# [46] 全排列
# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 理解全排列
        # 123
        # 求1开头的全排列
        #   求12开头的全排列 123、132
        # 213
        # 求2开头的全排列
        #   求21开头的全排列 213 231
        # 321
        # 求3开头的全排列
        #   求32开头的全排列 312 321
        # 核心是发生两次交换
        #   - 第一次交换是将开头的数字放在开头
        #   - 第二次是每次打头的数全排列结束后，恢复初始状态
        # 1234 1原地交换
        # 1234 1不变，2原地交换
        # 1234 12不变，3原地交换
        # 1234 123不变，4原地交换，起始点到达末尾 >> 1234，返回12不变
        # 1243 12不变，目标到达4，和起始点3交换，递归后起始点到达末尾，>> 1243
        # 1234 回溯，返回1不变，目标到达3，和起始点2交换
        # 1324 13不变，2原地交换
        # 1324 132不变，4原地交换，递归后起始点到达末尾，>> 1324
        # 1324 回溯
        # 1324 13不变，目标到达4，和起始点2交换
        # 1342 134不变，2原地交换，递归后起始点到达末尾，>> 1324
        def backtrack(first=0):
            # 求第n个数的全排列
            if first == n:
                result.append(nums[:])
            for i in range(first, n):
                # 交换：将需要开头的数字放在前面
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # 恢复前一个状态
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        result = []
        backtrack()
        return result