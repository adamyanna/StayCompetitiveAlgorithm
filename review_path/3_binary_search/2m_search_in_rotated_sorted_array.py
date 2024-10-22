#!/usr/bin/env python3

# Search in Rotated Sorted Array

"""
* 一次二分查找，其实就是将两次二分查找相结合，重点在于利用index0的值，先比较目标值和index的大小，确定是在分界点左边还是右边，然后二分，二分点如果大于index0，证明二分点在左，小于证明二分点在右边，这样就可以定位下一次二分是在左还是在右，二分点和目标值也要对比； 时间复杂度logn，二分查找快速选择都是logn
    * 分区的二分查找
    * 1. 处理所有可能出现的边界条件
        - 数组为空
        - 目标值为右边界值
        - 目标值为左边界值
        - 右边界值小于左边界，发生了反转，目标值在右、左之间，则不存在
    * 2. 定义 L、R 开始二分
    * 3. 定义退出条件：L=R，target 在L、R、M
    * 4. 对比 index0 index-1的大小确定是否发生了反转
    * 5. 如果无反转，则直接对比 target 和 indexM 更新 LR（regular BS）
    * 6. 如果有反转，则需要列出M在左升和右升的 2 种 case 下的各自3种condition
        - VindexM < Vindex-1 在右侧
        - VindexM > Vindex0 在左侧
        - m 如果比末尾值大，则在左侧
        -   那么 target 有3种情况
            - target 小于m值，且小于左值，那么target一定在m右侧 i = m+1
            - target 小于m值，且大于左值，那么target在m左侧 j = m-1
            - target 大于m，一定在旋转左侧 i，且在m右侧 = m+1
        - m 如果比末尾值小，则在右侧
            - target 小于 m 值，在左侧 j = m-1
            - target 大于 m 值，且小于最右值，在右侧 i = m+1
            - target 大于 m 值，同时大于最右值，在左侧 j = m-1
        - 其他情况均返回 - 1
"""


# Search in Rotated Sorted Array
# 搜索旋转排序数组

# 解法1: 两次二分查找，第一次找到分界点，数组中点i i-1 i+1 是否升序是否都比第一个数小，找到第一个比index0小的数字就向左边找； 找到分界点后再用二分搜索目标值
# 解法2: 一次二分查找，其实就是将两次二分查找相结合，重点在于利用index0的值，先比较目标值和index的大小，确定是在分界点左边还是右边，然后二分，二分点如果大于index0，证明二分点在左，小于证明二分点在右边，这样就可以定位下一次二分是在左还是在右，二分点和目标值也要对比； 时间复杂度logn，二分查找快速选择都是logn
# BS
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 获取数组长度
        length = len(nums)
        # 边界条件
        # 数组为空
        if not nums:
            return -1
        # 目标值为右边界值
        elif target == nums[length - 1]:
            return length - 1
        # 目标值为左边界值
        elif target == nums[0]:
            return 0
        # 右边界值小于左边界，发生了反转，单目标值在右、左之间，则不存在
        elif nums[length - 1] < nums[0] and nums[length - 1] < target < nums[0]:
            return -1
        else:
            pass

        # left & right
        i, j = 0, length -1
        while i <= j:
            m = i + (j - i) / 2
            # middle index

            mt= target
            mV= "M %s" % nums[m]
            mI= "I %s" % nums[i]
            mJ= "J %s" % nums[j]

            # 边界条件
            if target == nums[m]:
                return m
            elif target == nums[i]:
                return i
            elif target == nums[j]:
                return j
            elif i == j:
                return -1

            # 未反转的情况，直接通过二分查找返回结果
            if nums[length - 1] > nums[0]:
                # not rotated
                # 二分查找，更新左右值
                if target < nums[m]:
                    j = m -1
                else:
                    i = m + 1
            # 反转的情况
            else:
                # 反转的情况下，通过 binary 的方式有三种情况
                # 1. m在右侧的上升中，左 m 右
                # 2. m在右侧的上升中，左 m 右
                # 3. m正好在反转点上，m > L, m > R
                # 优先确定m在哪个位置上，判断条件只需要判断 m 是在左侧还是右侧
                # m 如果比末尾值大，则在左侧
                #   那么 target 有3种情况
                #      - target 小于m值，且小于左值，那么target一定在m右侧 i = m+1
                #      - target 小于m值，且大于左值，那么target在m左侧 j = m-1
                #      - target 大于m，一定在旋转左侧 i，且在m右侧 = m+1
                #
                # m 如果比末尾值小，则在右侧
                #      - target 小于 m 值，在左侧 j = m-1
                #      - target 大于 m 值，且小于最右值，在右侧 i = m+1
                #      - target 大于 m 值，同时大于最右值，在左侧 j = m-1
                # 其他情况均返回 - 1
                # rotated
                if nums[m] > nums[length -1]:
                    # middle on the left side
                    if target < nums[m] and target < nums[0]:
                        i = m + 1
                    elif nums[m] > target > nums[0]:
                        j = m - 1
                    elif target > nums[m]:
                        i = m + 1
                    else:
                        return -1
                elif nums[m] < nums[length -1]:
                    # middle on the right side
                    # or nums are not rotated
                    if target < nums[m]:
                        j = m - 1
                    elif target > nums[m] and target > nums[0]:
                        j = m - 1
                    elif nums[m] < target < nums[0]:
                        i = m + 1
                    else:
                        return -1

        return -1