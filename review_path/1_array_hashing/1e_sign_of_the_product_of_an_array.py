#!/usr/bin/env python3

# Sign of the Product of an Array
# * 有0结果为0
# -1 需要考虑遍历负数的次数，odd = -1 even = 1
# 以上都不是，结果为1

class Solution:
    def arraySign(self, nums):
        result = 1
        for v in nums:
            if v == 0:
                return 0
            if nums < 0:
                result = -result

        return result

# Golang
# func arraySign(nums []int) int {
# 	pro = 1
# 	for i:=0;i<len(nums);i++{
# 		if nums[i] == 0 {
# 			return 0
# 		}
# 		if nums[i] < 0 {
# 			// odd number of -
# 			// even number of +
# 			pro = -pro
# 		}
# 	}
# 	return pro
#
# }
