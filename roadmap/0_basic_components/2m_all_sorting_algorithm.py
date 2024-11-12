#!/usr/bin/env python3

"""
快速排序
    利用二分法，每次的基准数和其他数比较大小，找到自己位置，在对两边做二分递归。时间复杂度使用主定理
桶排序
    0～n之间的数，要n个桶，每个桶装和自己序号相等的数的数量，最后遍历桶，将数展开；m+n m是桶长度
冒泡排序
    每次两两比较，将最大数放在最后一个位置，然后继续找第二大的数，用n**2的时间复杂度，将所有的数冒泡到自己的位置
堆排序
    堆是具有以下性质的完全二叉树：
        每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。
    a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;
    b.将堆顶元素与末尾元素交换，将最大元素”沉”到数组末端;
    c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。
"""
def quick_sort(nums):
    """
    Quick Sorting
    :param nums:
    :param start:
    :param end:
    :return:
    """

    if len(nums) <= 1:
        return nums

    return quick_sort([v for v in nums[1:] if v <= nums[0]]) + [nums[0]] + quick_sort([v for v in nums[1:] if v > nums[0]])


def heap_sort(nums):
    pass


if __name__ == '__main__':
    print(quick_sort([54, 26, 26, 93, 17, 77, 31, 44, 55, 20]))