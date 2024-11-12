#!/usr/bin/env python3

class Solution(object):
    def sub_arrays_with_k_different_int(self, nums, k):
        """
        输入：nums = [1,2,1,2,3], k = 2
        输出：7
        解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

        输入：nums = [1,2,1,3,4], k = 3
        输出：3
        解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].

        :param nums:
        :param k:
        :return:
        """

        def handler(nums, k):
            """
            get most k count array
            [1,2,1,2,3], 2
            1 & 1,2 & 1,2,1 & 1,2,1,2 == 4
            2 & 2,1 & 2,1,2 == 3
            1 & 1,2 == 2
            2 & 2,3 == 2
            3 == 1
            12 - 5 = 7
            """
            """
            MARK-Tricky !!! [当前数组从L到R，以L为起点的所有子数组的个数为 R - L + 1]
            Analyze
            1. 
            分析
             - 利用滑动窗口的方式，将窗口一直保持在k个不同字符的范围内
             - 窗口两端下标的差值 + 1，表示当前窗口内，从左边开始的所有子数组数量
             - handler(nums, k) - handler(nums, k - 1)
            1. 定义 l，r，size 为窗口的两端和大小，先移动 r，并记录当前移动 r 的过程中重复字符的出现次数，每一次非重复字符的出现表示 size + 1
                    - r 每一次移动都记录当前size内，所有 k 以内的子数组数量 = r - l + 1
            2. 当 size 大小超过 k，则移动 l，并且更新记录的字符次数，并且更新size大小
            3. traversal array
            """
            # use a l & r & size to track
            l, current_size = 0, 0
            counter_map = {}
            result = 0
            # move r
            for r in range(len(nums)):
                if counter_map.get(nums[r], 0) == 0: # first time occurrence
                    current_size += 1
                counter_map[nums[r]] = counter_map.get(nums[r], 0) + 1 # update counter
                # move l to keep window size
                while current_size > k:
                    counter_map[nums[l]] -= 1
                    if counter_map[nums[l]] == 0:
                        current_size -= 1
                    # move l for every loop
                    l += 1
                # size to most k sub array number
                result += (r - l) + 1

            return result

        if k == 1:
            return handler(nums, k)
        else:
            return handler(nums, k) - handler(nums, k - 1)





        #     counter = {}  # save current char occurrence time
        #     l, result = 0, 0
        #     current_range = 0
        #     for r in range(len(nums)):
        #         # update current range for diff num
        #         if counter.get(nums[r], 0) == 0:
        #             current_range += 1
        #         # update number occurrence
        #         counter[nums[r]] = counter.get(nums[r], 0) + 1
        #         while current_range > k:
        #             # update left
        #             counter[nums[l]] -= 1
        #             if counter[nums[l]] == 0:
        #                 current_range -= 1
        #             l += 1
        #         result += (r - l + 1)
        #         print(l, r, result)
        #     return result
        #
        # if k - 1 == 0:
        #     return handler(nums, k)
        # result1 = handler(nums, k)
        # print("K: %d -> %d" % (k, result1))
        # result2 = handler(nums, k-1)
        # print("K: %d -> %d" % (k-1, result2))
        #
        # return result1 - result2

        # length = len(nums)
        # result = 0
        # for l in range(length):
        #     r = l - 1
        #     k_set = set()
        #     # if l > 0:
        #     #     k_set.remove(nums[l - 1])
        #     while r + 1 < length:
        #         if len(k_set) < k:  # [1,2,1,2,3]
        #             k_set.add(nums[r + 1])
        #             if k == len(k_set): result += 1
        #         elif k == len(k_set) and nums[r + 1] in k_set:
        #             result += 1
        #         r += 1
        #
        # return result

if __name__ == '__main__':
    print(Solution().sub_arrays_with_k_different_int([1,2,1,2,3], 2))
    print(Solution().sub_arrays_with_k_different_int([1,2,1,3,4], 3))
    print(Solution().sub_arrays_with_k_different_int([2, 1, 1, 1, 2], 1))
