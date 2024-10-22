#!/usr/bin/env python3

# find-median-from-data-stream

##############################
# Understand python.heapq
import heapq
def py_heap_test(unsorted_array):
    head = []
    for v in unsorted_array:
        heapq.heappush(head, v)
    heap_sort = [heapq.heappop(head) for _ in range(len(head))]
    print(heap_sort)

if __name__ == '__main__':
    py_heap_test([1, 9, 7, 8, 3, 6 ,10])


# 堆
# 一个完全二叉树
# 大顶堆：每个结点的值都大于或者等于左右孩子结点的值
# 小顶堆：每个结点的值都小于或者等于左右孩子节点的值
# headpop -> 将 heap 顶部 pop 出，并将剩余 element 转为 小顶
# headpush -> 将 element push 入 heap，并保持小顶

##############################
# find-median-from-data-stream.CN
# 0. trick: 用两个堆，分别存中位数的左右值，为了每次通过 pop 拿到左边最大的元素放入右边，则用-负值存储左边的堆
# 1. 初始化两个 list， 分别用于存储中位数的左右值，左边应该总比右边小
# 2. 每增加一个数字就对比是否比左堆堆中最大的数字小，如果是就 push 入左边
#    - 并且对比左右长度，利用 heappush 和 heappop 更新
# 3. 大于左边最大值，就对右边做相同操作
# 4. 中位数就是左右 heap 的 0index 值或平均值
##############################

"""
Tricky!!!
use negative values to store Max heap
"""

class MedianFinder:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if not queMin_ or num <= -queMin_[0]:
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_):
                heapq.heappush(queMax_, -heapq.heappop(queMin_))
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        return (-queMin_[0] + queMax_[0]) / 2