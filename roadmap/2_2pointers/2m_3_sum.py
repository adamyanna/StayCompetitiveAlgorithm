#!/usr/bin/env python3

# 3Sum
# 三数之和为0，对数组做排序，选定一个k（从index0开始），从k的前一个位置开始和数组末尾的位置开始L，R，三数相加如果大于0，则移动R-1，反之L+1，保存所有满足0的组合结果
# 1. 对数组做排序
# 2. 处理边界条件
#   - 数组存在 & 数组长度大于2 & 数组第k个元素小于0 & k 小于index-1
#   - index0 值大于0直接return
# 3. 最外层循环只遍历小于等于0的值，如果遇到大于0的值直接跳出
# 4. 对于基准k也需要进行对其前一个元素的对比和去重复，遇到重复直接前移一个元素，去除重复答案
# 5. L ptr 起点为 k+1， R ptr 起点为 -1 index ，内循环到i j 相遇为止
# 6. 双指针 i 向右移动 j向左移动，获取当前位置下三数之和，处理三种情况
#   - 1. 相加之和小于0，i向右移动，且如果遇到相同的数字需要去重复
#   - 2. 相加之和大于0，j向左移动，且去重
#   - 3. 相加之和=0，保存结果，并同时移动i，j，并同时去重
# 7. 基准从index0开始，没完成一次就+1

# 3Sum
# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort and 2 points

        # 对数组排序
        # 处理边界条件
        # - 数组存在 & 数组长度大于2 & 数组第k个元素小于0 & k 小于index-1
        # k 从 index 0 开始
        # index0 值大于0直接return
        #

        result = []
        nums.sort() #nlog(n)
        k = 0
        while nums and len(nums) > 2 and nums[k] <= 0 and k < len(nums) -1: # n
            if nums[k] > 0: break # 最外层循环只遍历小于等于0的值，如果遇到大于0的值直接跳出
            # 对于基准k也需要进行对其前一个元素的对比和去重复
            # 遇到重复直接前移一个元素，去除重复答案
            if k != 0 and nums[k] == nums[k-1]: k+=1; continue

            # L ptr 起点为 k+1
            # R ptr 起点为 -1 index
            i = k + 1
            j = len(nums) -1
            # 循环到i j 相遇为止
            while i < j:
                # 双指针 i 向右移动 j向左移动
                # 获取当前位置下三数之和
                s = nums[i] + nums[k] + nums[j]
                # 处理三种情况
                # 1. 相加之和小于0，i向右移动，且如果遇到相同的数字需要去重复
                if s < 0:
                    i += 1
                    while i <j and nums[i] == nums[i - 1]: i += 1 # 去重
                # 2. 相加之和大于0，j向左移动，且去重
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1 # 去重
                # 3. 相加之和=0，保存结果，并同时移动i，j，并同时去重
                else:
                    t = [nums[i], nums[k], nums[j]]
                    result.append(t)
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
            # 基准从index0开始，没完成一次就+1
            k += 1

        return result


    # T: nlog(n) + n**2  == n**2