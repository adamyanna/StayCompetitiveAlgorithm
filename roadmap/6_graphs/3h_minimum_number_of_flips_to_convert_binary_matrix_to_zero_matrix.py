#!/usr/bin/env python3
import queue


# TODO
# https://leetcode.cn/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/solutions/101359/zhuan-hua-wei-quan-ling-ju-zhen-de-zui-shao-fan-2/
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
# 转化为全零矩阵的最少反转次数

class Solution(object):

    def minFlips(self, mat: list[list[int]]) -> int:

        def convert_matrix_to_hashable(matrix):
            """
            convert matrix to a binary
            if check result == 0
            :param matrix:
            :return:
            """
            check_result = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    check_result = matrix[i][j] + check_result * 2
            return check_result

        def convert_hashable_binary_back_to_matrix(binary, m, n):
            matrix = [[0] * n for _ in range(m)]
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    matrix[i][j] = binary & 1
                    binary >>= 1
            return matrix

        def do_flip(current_m, m, n, i, j):
            for a, b in ((i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= a < m and 0 <= b < n:
                    current_m[a][b] = current_m[a][b] ^ 1

        def min_flip(matrix):
            m = len(matrix)
            n = len(matrix[0])

            result = 0
            q = queue.Queue()
            start_m_b = convert_matrix_to_hashable(matrix)
            if start_m_b == 0:
                return result
            q.put(start_m_b)
            visited = set()
            visited.add(start_m_b)

            while not q.empty():
                result += 1
                q_size = q.qsize()
                for _ in range(q_size):
                    current_m = convert_hashable_binary_back_to_matrix(q.get(), m, n)
                    for i in range(m):
                        for j in range(n):
                            do_flip(current_m, m, n, i, j)
                            new_m_b = convert_matrix_to_hashable(current_m)
                            if new_m_b == 0:
                                return result
                            if new_m_b not in visited:
                                visited.add(new_m_b)
                                q.put(new_m_b)
                            do_flip(current_m, m, n, i, j)
            return -1

        return min_flip(mat)


if __name__ == '__main__':
    # [0,0]
    # [0,1]
    light = [[0, 0], [0, 1]]
    print(Solution().minFlips(light))

    # check_result = 0
    # for i in range(len(light)):
    #     for j in range(len(light[0])):
    #         check_result = light[i][j] + check_result * 2
    # print(check_result)
    #
    # matrix = [[0] * 2 for _ in range(2)]
    # for i in range(2 - 1, -1, -1):
    #     for j in range(2 - 1, -1, -1):
    #         matrix[i][j] = check_result & 1
    #         check_result >>= 1
    # print(matrix)


