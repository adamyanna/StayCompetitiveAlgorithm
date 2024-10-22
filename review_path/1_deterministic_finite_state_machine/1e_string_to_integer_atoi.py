#!/usr/bin/env python3

# String to Integer (atoi)
# 有限状态自动机 - 求解
# 分析
# 1. 转换规则编写子函数
# 2. 溢出的整数无法对比大小，考虑 target x 10 之前，对 target 和 INT_MAX 对比
# 自动机的实现
# 确定性有限状态自动机 Deterministic Finite State Machine/Automaton
# Automaton 状态定义
# --------- | white space | +/- | 0~9 | other
# start     | start | signed | in_number | end
# signed    | end | end | in_number | end
# in_number | end | end | in_number | end
# end       | end | end | end | end


INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans


# # String to Integer (atoi)
# INT_MAX = 2 ** 31 - 1
# INT_MIN = -2 ** 31
# class Solution(object):
#     def myAtoi(self, string):
#         """
#         :type str: str
#         :rtype: int
#         """
#         # Anylize
#         #  special: return 0
#         # int32
#         s = s.strip()
#         if not s:
#             return 0
#         l = [str(i) for i in xrange(10)]
#         result = 0
#         sign = 1
#         if s[0] == "-":
#             sign = -1
#         for i in range(0, len(s)):
#             v = s[i]
#             if i == 0 and v in ["-", "+"]:
#                 continue
#             if v in l:
#                 if sign == -1:
#                     if (INT_MIN + int(v)) // 10 >= result:
#                         result = INT_MIN
#                         break
#                     result = result * 10 + (int(v) * sign)
#                 else:
#                     if (INT_MAX - int(v)) // 10 <= result:
#                         result = INT_MAX
#                         break
#                     result = result * 10 + int(v)
#             else:
#                 break
#         return result