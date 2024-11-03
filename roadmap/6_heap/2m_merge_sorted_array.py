#!/usr/bin/env python3

# merge-k-sorted-array

class Solution1(object):
    def merge_k_sorted_array(self, *num_lists):
        new_list = []
        for nums in num_lists:
            new_list.extend(nums)
        return sorted(new_list)


class Solution2(object):
    def merge_k_sorted_array(self, num_lists):
        def merge(l1, l2):
            """
            1,3,6
            2,4,5,7
            :param l1:
            :param l2:
            :return:
            """
            new_l = []
            p1, p2 = 0, 0
            while p1 < len(l1) or p2 < len(l2):
                if p1 == len(l1):
                    new_l.append(l2[p2])
                    p2 += 1
                elif p2 == len(l2):
                    new_l.append(l1[p1])
                    p1 += 1
                elif l1[p1] < l2[p2]:
                    new_l.append(l1[p1])
                    p1 += 1
                else:
                    new_l.append(l2[p2])
                    p2 += 1
            return new_l
        if len(num_lists) >= 2:
            return self.merge_k_sorted_array(num_lists[1:-1] + [merge(num_lists[0], num_lists[-1])])
        elif len(num_lists) == 1:
            return num_lists[0]
        else:
            return []

import heapq
class Solution3(object):
    def merge_k_sorted_array(self, array_lists):
        result_l = []
        min_heap = []
        for array_count, array in enumerate(array_lists):
            if not array: continue
            start_index = 0
            heapq.heappush(min_heap, (array[0], array_count, start_index))

        while len(min_heap):
            min_value, array_count, array_index = heapq.heappop(min_heap)
            result_l.append(min_value)
            # update heap
            if array_index + 1 < len(array_lists[array_count]):
                heapq.heappush(min_heap, (array_lists[array_count][array_index + 1], array_count, array_index + 1))

        return result_l

class CustomHeap(object):
    def __construct_min_heap(self, array):
        def adjust(a, m, i):
            head = i
            l = 2*i + 1
            r = 2*i + 2
            if l < m and a[i][0] > a[l][0]:
                head = l
            if r < m and a[head][0] > a[r][0]:
                head = r
            if head != i:
                a[head], a[i] = a[i], a[head]
                adjust(a, m, head)
        m = len(array)
        for i in range(m, -1, -1):
            adjust(array, m, i)

    def heap_push(self, array, element):
        array += [element]
        self.__construct_min_heap(array)

    def heap_pop(self, array):
        result = array.pop(0)
        self.__construct_min_heap(array)
        return result


class Solution4(object):
    def merge_k_sorted_array(self, array_lists):
        hp_instance = CustomHeap()
        result_l = []
        min_heap = []
        for array_count, array in enumerate(array_lists):
            if not array: continue
            start_index = 0
            hp_instance.heap_push(min_heap, (array[0], array_count, start_index))

        while len(min_heap):
            min_value, array_count, array_index = hp_instance.heap_pop(min_heap)
            result_l.append(min_value)
            # update heap
            if array_index + 1 < len(array_lists[array_count]):
                hp_instance.heap_push(min_heap, (array_lists[array_count][array_index + 1], array_count, array_index + 1))

        return result_l

"""
TimeComplexAnalyze

construct min heap time cost logK
all number is N

=> O(NlogK)

"""

if __name__ == '__main__':
    result1 = Solution3().merge_k_sorted_array([[1,3,6,64],[2,4,5,7,99],[17, 20, 26, 31, 44, 54, 55, 77, 93]])
    result2 = Solution4().merge_k_sorted_array([[1,3,6,64],[2,4,5,7,99],[17, 20, 26, 31, 44, 54, 55, 77, 93]])
    print(result1 == result2)