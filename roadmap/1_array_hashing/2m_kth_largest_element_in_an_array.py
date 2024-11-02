#!/usr/bin/env python3

# kth-largest-element-in-an-array


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        1. use heap
        2. use quick sorting
        :param nums:
        :param k:
        :return:
        """

        # method 1.1
        # result = None
        # import heapq
        # large_heapq = []
        # for v in nums: # use negative value to store as a large top heap
        #     heapq.heappush(large_heapq, -v)
        # for i in range(k):
        #     result = -heapq.heappop(large_heapq)
        # return result

        # method 1.2 construct heap push & pop


        # use quick sorting
        import random

        def partition(l, r, p):
            """
            partition & return p index
            :param l:
            :param r:
            :param p:
            :return:
            """
            p_value = nums[p]
            nums[p], nums[r] = nums[r], nums[p] # move p value to end
            exchange_i = l
            for i in range(l, r):
                if nums[i] < p_value:
                    nums[i], nums[exchange_i] = nums[exchange_i], nums[i]
                    exchange_i += 1 # move all smaller to front
            nums[r], nums[exchange_i] = nums[exchange_i], nums[r] # move p_value back to partition center

            return exchange_i

        def quick_selection(l, r, k):
            p = random.randint(l, r)
            # do a partition once
            p = partition(l, r, p)
            if k == p:
                return nums[p]
            elif k < p:
                return quick_selection(l, p, k)
            else:
                return quick_selection(p, r, k)

        return quick_selection(0, len(nums) - 1, len(nums) - k)

if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))