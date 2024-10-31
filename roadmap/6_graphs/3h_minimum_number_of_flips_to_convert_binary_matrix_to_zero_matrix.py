#!/usr/bin/env python3

# TODO
# https://leetcode.cn/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/solutions/101359/zhuan-hua-wei-quan-ling-ju-zhen-de-zui-shao-fan-2/
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
#  转化为全零矩阵的最少反转次数

# class Solution():
#
#   def get_all_light_off(self, light):
#       # graph BFS
#
#
#       def do_flip(light_status):
#           if light_status == 1:
#               return 0
#           else:
#               return 1
#
#       queue = list()
#       first_on_light_i = None
#       first_on_light_j = None
#
#
#       for i in range(light):
#           for j in range(light[0]):
#               if light[i][j] == 1:
#                   first_on_light = light[i][j]
#
#       queue.append(first_on_light)
#
#       while len(queue) > 0:
#
#           on_light = queue.pop(0)
#               # up
#               if do_flip(light[i-1][j]) == 1:
#                   queue.append(light[i-1][j])
#               # bottom
#               if do_flip(light[i+1][j]) == 1:
#                   queue.append(light[i+1][j]
#               # left
#               if do_flip(light[i][j-1]) == 1
#                   queue.append(light[i][j-1])
#               # right
#               if do_flip(light[i][j+1]) == 1
#                   queue.append(light[i][j+1])
#
#
#           elif light[i][j] == 0:
#               pass


# if __name__ == '__main__':
#
#     light = [
#     [0, 1, 1],
#     [0, 1, 0],
#     [0, 1, 1],
#     ]
#     Solution().get_all_light_off(light)