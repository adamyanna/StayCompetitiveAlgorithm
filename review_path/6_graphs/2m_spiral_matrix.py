#!/usr/bin/env python3

# Spiral Matrix
"""
* 模拟旋转，暴力将原矩阵上右下左切除，最终留下的一个元素就是tail
* 将平面中从左向右的方向定义为 +x
* 将平面中从上倒下的防线定义为 -y
* +x = m[0]
* -y = for i in range(len(m)): m[i][-1]
* -x = m[-1] reverse
* +y = for i in range(len(m)): m[i][0] reverse
* 利用 pop 将会影响后续循环的部分切除
* 考虑三种边界条件，m操作后为空，-y -x操作后m尾部空array，+y操作后m头部为空
"""
# Spiral Matrix
# input: [[1,2,3],[4,5,6],[7,8,9]]
# [1,2,3]
# [4,5,6]
# [7,8,9]
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # 模拟旋转
        # TODO

        # 将平面中从左向右的方向定义为 +x
        # 将平面中从上倒下的防线定义为 -y
        # +x = m[0]
        # -y = for i in range(len(m)): m[i][-1]
        # -x = m[-1] reverse
        # +y = for i in range(len(m)): m[i][0] reverse
        # 利用 pop 将会影响后续循环的部分切除
        result = []
        while matrix:
            # +x 并 pop
            if not result:
                result = matrix.pop(0)
            else:
                result.extend(matrix.pop(0))

            # 边界条件（考虑边界条件的位置）
            if not matrix:
                return result

            # -y 并 pop
            for s in range(len(matrix)):
                result.append(matrix[s][-1])
                matrix[s].pop(-1)

            # -x 并 pop
            for _ in range(len(matrix[-1])):
                result.append(matrix[-1][-1])
                matrix[-1].pop(-1)

            # 边界条件（尾部数组为空后需要pop）
            while matrix and not matrix[-1]:
                matrix.pop(-1)

            # +y reverse [len(m) - 1 - i][0] & pop
            for j in range(len(matrix)):
                result.append(matrix[len(matrix) - 1 - j][0])
                matrix[len(matrix) - 1 - j].pop(0)

            # 边界条件（头部数组为空后需要pop） -> TODO
            while matrix and not matrix[-1]:
                matrix.pop(-1)
        return result