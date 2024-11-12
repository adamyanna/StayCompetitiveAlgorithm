#!/usr/bin/env python3

class Solution:
    def smallestDifference(self, a, b):
        a.sort()
        b.sort()
        result = float('inf')
        i, j = 0, 0
        while i < len(a) and j < len(b):
            # get minimum result from absolute value
            result = min(result, abs(a[i] - b[j]))
            # update i for larger value
            if a[i] < b[j]:
                i += 1
            # update j for larger value
            else:
                j += 1

        return result





if __name__ == '__main__':
    # 输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
    # 输出：3，即数值对(11, 8)
    print("%f" % float('inf'))
    print(Solution().smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))
