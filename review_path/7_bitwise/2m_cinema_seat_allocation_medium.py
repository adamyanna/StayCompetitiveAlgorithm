#!/usr/bin/env python3

# Cinema Seat Allocation  Medium
"""
* 按照可用位置为0，不可用位置为1的方式，通过0b，枚举三种复合条件的情况
* 将reserved转为dict，k为row，v为座位的位置的数组[]，遍历dict，并对座位号码通过bitwise操作，1表示占用，在二进制中左移 1<<i-2；
* 以上步骤2可以合并为一个步骤，对每一行汇总所有的8位的二进制使用 或操作，聚合
* dict长度为有占用的row数量，(n-row)x2 既可以得出无权没有被预订的行的最大结果（2）
* 对dict中所有行的 bitwise 占座循环和枚举的三种情况进行或运算，预期结果仍然为枚举情况时，表示预期的0空位并未被占用，否则即表示被占用
* 以上三种枚举任意一种在一行中成立即可 结果+1
"""


# Cinema Seat Allocation
# 安排电影院座位
# 返回 最多能安排多少个 4 人家庭 。4 人家庭要占据 同一行内连续 的 4 个座位（支持拆成过道两边各坐 2 人）

# 输入：n 行座位 & 预定的座位的location
# 思路：
# 1. 找到每一行连续超过4个无人预定的座位
# 2. 在无人预定的座位中，找多所有组合，枚举三种：4-7，2-3+4-5，6-7+8-9
# 3. 输出结果
# 思路2: bitwise method
# 位运算：<< 左移动, >> 右移动，云算数在符号左边，右边为移动的位移量
# review bitwise
# - | 有1就为1
# - & 都是1才为1
# - ^ 不同为1，相同为0
# - ~ 按位取反
# - << 左移,云算数在符号左边，右边为移动的位移量
# - >> 右移,云算数在符号左边，右边为移动的位移量


import collections
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # 枚举三种情况（0b表示该整形为二进制）
        # 其中0表示未被预定的可用位置
        left, middle, right = 0b11110000, 0b11000011, 0b00001111
        occupied = collections.defaultdict(int)
        for seat in reservedSeats:
            # reserve 最两端的位置对结果完全没有影响
            if 2 <= seat[1] <= 9:
                # 将每一行预定的座位转换为二进制位
                # 每行座位最大处是：2进制高位，左移增大
                # 除去两边的1、10，剩下的用来表示当前8位二进制，从2开始，所以要减去起始位置， 1 << i -2
                # 通过按位或，得出没行所有预定位置的二进制表示
                occupied[seat[0]] |= (1 << (seat[1] - 2))

        # n - 预定行数 * 2 = 无人预定行可以得到的最多结果
        ans = (n - len(occupied)) * 2
        # 访问每一行的 bitwise，
        # 假设第9个位置的 bitwise = 0b10000000
        # 每个bitwise 和任意一种枚举情况做 或操作 ，如果或操作的结果和原始结果不相等，则表示枚举中的0空位，被占用了
        for row, bitmask in occupied.items():
            if (bitmask | left) == left or (bitmask | middle) == middle or (bitmask | right) == right:
                ans += 1
        return ans