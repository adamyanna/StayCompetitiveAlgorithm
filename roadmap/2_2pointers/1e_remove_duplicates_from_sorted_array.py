#!/usr/bin/env python3

"""
remove-duplicates-from-sorted-array

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

原地 删除重复出现的元素
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        double pointer & in-place algorithm

        [0,0,1,1,1,2,2,3,3,4]
         0   2
        :param nums:
        :return:
        """
        if not nums: return 0
        m = len(nums)
        i = 0
        result = 0
        while i < m:
            j = i + 1
            result += 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            if i + 1 < j:
                if j < len(nums):
                    # repeat num occur
                    # in-place swap/exchange
                    nums[i+1:] = nums[j:] + nums[i+1:j]
                else:
                    # j out of index, no need to swap
                    break
                m -= (j - i - 1)
            # update i
            i += 1

        return result


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))
    print(nums)