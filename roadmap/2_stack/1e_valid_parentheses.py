#!/usr/bin/env python3

# Valid Parentheses
# 使用栈的数据结构，对比栈顶元素是否是当前类型的括号
# 定义括号类型，用整形表示同一种类型，用L、R表示左右
# 初始化一个 list 作为栈
# 遍历每一个字符，如果字符出现左括号，则入栈append，如果字符出现有括号且当前栈为空，则直接返回 F
# 如果字符出现有括号，且栈非空，对比当前栈顶元素是否是同一种类型括号
#   - 是：pop出、继续loop
#   - 否：返回 False

#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. from 0 to n > and find it's pair X
        # 1. L, R
        # 2. 1,2,3 reverse 3,2,1

        stack = []
        q_dict = {
            "(": (1, "L"),
            ")": (1, "R"),
            "[": (2, "L"),
            "]": (2, "R"),
            "{": (3, "L"),
            "}": (3, "R")
        }
        for v in s:
            if q_dict[v][1] == "R":
                if not stack:
                    return False
                else:
                    if q_dict[v][0] == stack[-1:][0][0]:
                        stack.pop(len(stack) - 1)
                    else:
                        return False
            else:
                stack.append(q_dict[v])
        if not stack:
            return True
        return False


# @lc code=end