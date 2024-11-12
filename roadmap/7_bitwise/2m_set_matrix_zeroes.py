#!/usr/bin/env python3

"""
set-matrix-zeroes

给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

常量空间 O(1) space complexity
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        bitwise solution
        0110
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]: return


        # get entire matrix bit map
        matrix_bit_map = int("".join(["1"] * len(matrix[0])), 2)
        current_bit_map = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # update current bitwise
                    current_bit_map = current_bit_map << 1
                else:
                    current_bit_map = current_bit_map << 1
                    current_bit_map += 1
            matrix_bit_map &= current_bit_map
            current_bit_map = 0

        for i in range(len(matrix)):
            str_index_bit_map = str(bin(matrix_bit_map)).lstrip("0b")
            str_index_bit_map = "".join(["0"] * (len(matrix[i]) - len(str_index_bit_map))) + str_index_bit_map
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    # set [i][j] in-place all 0
                    matrix[i] = [0] * len(matrix[i])
                    break
                if str_index_bit_map[j] == "0":
                    matrix[i][j] = 0


if __name__ == '__main__':
    # # 1
    # # 110
    # # 1111
    # print("%d %d" % (int("1111", 2), int("110", 2)))
    # print(f"{(0 << 1):b}")
    # print("{:b}".format(15 & 6))
    # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Solution().setZeroes(matrix)
    print(matrix)
