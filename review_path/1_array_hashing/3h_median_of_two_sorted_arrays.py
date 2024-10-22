#!/usr/bin/env python3

# 寻找两个有序数组的中位数

# 分析
# 获取两个有序序列第 k 个最小的数
# 思路
# 二分法， 对比两个数组第 m = k/2 - 1 处的大小，
# 如果num1[m] < num2[m] 则第k小的数字一定不会出现在num1[0...m],
# 反之num1[m] > num2[m]则 第k小的数字一定不会出现在num2[0...m]

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p = 0
        if nums1:
            for n2 in nums2:
                # 定义左右ptr 0 和 -1 开始
                n = p
                m = len(nums1) - 1
                while True:
                    # 循环内对 nums1 二分
                    i = int((m - n) / 2) + n
                    #
                    if n == m:
                        if n2 > nums1[n]:
                            p = n + 1
                            break
                        else:
                            p = n
                            break
                    if n == m - 1:
                        if nums1[n] <= n2 <= nums1[m]:
                            p = n + 1
                            break
                        elif n2 < nums1[n]:
                            p = n
                            break
                        elif n2 > nums1[m]:
                            p = m + 1
                            break
                        else:
                            break

                    # 如果外部循环内 for 的 nums 找到了 二分值，则将 nums2 的值更新到nums1
                    if n2 == nums1[i]:
                        p = i
                        break
                    elif n2 < nums1[i]:
                        m = i
                    else:
                        n = i
                nums1.insert(p, n2)
        else:
            nums1 = nums2
        if len(nums1) % 2 > 0:
            return nums1[int(len(nums1) - 1) / 2]
        else:
            return float((nums1[int(len(nums1) / 2)] + (nums1[int(len(nums1) / 2 - 1)])) / 2.0)


# 寻找两个正序数组的中位数
# median-of-two-sorted-arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            # 定义两个起始坐标，用于标记每次对比后，将被 del 的元素
            index1, index2 = 0, 0

            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                # 取边缘和 k//2 -1 最小的下标 index
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                # 获取 m = k/2 - 1 处的值
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                # 对比大小
                # 1. 如果 1 <= 2, 就更新k的值，k从第k大的，更新为第 k - (k/2-1), 并更新起始坐标
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                # 2. 如果 1 > 2, 对k的值做相同的操作（基于 nums2 起始坐标）
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2
