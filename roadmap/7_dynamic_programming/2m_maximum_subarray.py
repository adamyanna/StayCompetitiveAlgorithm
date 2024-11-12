#!/usr/bin/env python3

class Solution:

    # dp[i] = max(dp[i-1] + nums[i], nums[i])
    # result = f{dp[i]...}
    # MARK-tricky: use nums[i] to store current max on i
    def maxSubArray(self, nums):
        if not nums: return 0
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] > nums[i]:
                # current max at index i
                # use index i to store current max
                nums[i] = nums[i] + nums[i - 1]

            result = max(result, nums[i])
        print(nums)
        return result


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

