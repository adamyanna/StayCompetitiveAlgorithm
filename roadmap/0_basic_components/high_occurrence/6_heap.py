#!/usr/bin/env python3

import heapq
import queue


class Solution(object):
    def heap_review(self, unsorted_array):
        heap_list = []
        for v in unsorted_array:
            heapq.heappush(heap_list, v)
        for _ in range(len(heap_list)):
            print(heapq.heappop(heap_list))

    def queue_review(self, unsorted_array):
        self.this_queue = queue.Queue()
        for v in unsorted_array:
            self.this_queue.put(v)
        while not self.this_queue.empty():
            print(self.this_queue.get())

def heap_adjust(array, m, i):
    # left child -> 2*i+1
    # right child -> 2*i+2
    largest = i
    l = 2 * i + 1  # left child -> 2*i+1
    r = 2 * i + 2  # right child -> 2*i+2

    if l < m and array[i] < array[l]:
        largest = l

    if r < m and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # 交换

        heap_adjust(array, m, largest)

def heap_sort(nums):
    if not nums: return nums
    m = len(nums)
    for i in range(m):
        heap_adjust(nums, m, i)
        print(nums)

    return heap_sort(nums[1:]) + [nums[0]]

def construct_large_heap(array):

    def heap_adjust(array, m, i):
        head = i
        l = 2*i + 1
        r = 2*i + 2
        if r < m and array[i] < array[l]:
            head = l
        if r < m and array[head] < array[r]:
            head = r

        if head != i:
            array[i], array[head] = array[head], array[i]
            heap_adjust(array, m, head)

    n = len(array)
    for i in range(n, -1, -1):
        heap_adjust(array,n,i)
    return array


def construct_small_heap(nums):

    def heap_adjust(array, m, i):
        head = i
        l = 2*i + 1
        r = 2*i + 2
        if l < m and array[i] > array[l]:
            head = l
        if r < m and array[head] > array[r]:
            head = r

        if head != i:
            array[head], array[i] = array[i], array[head]
            heap_adjust(array, m, head)

    n = len(nums)
    for i in range(n, -1, -1):
        heap_adjust(nums, n, i)
    return nums

def heap_sort_min(nums):
    if not nums: return nums
    n_nums = construct_small_heap(nums)
    return [n_nums[0]] + heap_sort_min(n_nums[1:])

if __name__ == '__main__':
    # Solution().heap_review([54, 26, 93, 17, 77, 31, 44, 55, 20])
    # print("#"*20)
    # Solution().queue_review([54, 26, 93, 17, 77, 31, 44, 55, 20])
    #
    # # sorting
    # print(heap_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
    #
    # maximum heap
    print(construct_large_heap([54, 26, 93, 17, 77, 31, 44, 55, 20]))

    # minimum heap
    print(construct_small_heap([54, 26, 93, 17, 77, 31, 44, 55, 20]))
    print(heap_sort_min([54, 26, 93, 17, 77, 31, 44, 55, 20]))