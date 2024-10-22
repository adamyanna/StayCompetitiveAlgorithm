#!/usr/bin/env python3

# Longest Palindromic Substring
"""
* 中心扩展法
* 动态规划
* 从一个中心点开始向两端扩算，计算出该点的最长回文串的长度，并hash存储长度-string值的结果
* for 循环所有的字符，将每一个字符作为一次扩散的中心点
* 同时在一次循环中处理两种扩散条件
* 1. ABA，odd，需要处理L=i-1，R=i+1的情况
* 2. AA， even，需要处理L=i，R=i+1的情况
* 两种情况的循环中中需要：1. 考虑边界条件 2. L、R值相等 3. 更新LR、更新结果串左右拼接
* 最终在hash结果中选择maxk的结果返回即可
* 边界条件：s长度为1 直接返回
"""


# 回文 - 中心扩散法

#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # A: find the same from start to end as start of iterable
        # 分析
        # 从一个中心点开始向两端扩算，计算出该点的最长回文串的长度，并hash存储长度-string值的结果
        # for 循环所有的字符，将每一个字符作为一次扩散的中心点
        # 同时在一次循环中处理两种扩散条件
        # 1. ABA，odd，需要处理L=i-1，R=i+1的情况
        # 2. AA， even，需要处理L=i，R=i+1的情况
        # 两种情况的循环中中需要：1. 考虑边界条件 2. L、R值相等 3. 更新LR、更新结果串左右拼接
        # 最终在hash结果中选择maxk的结果返回即可
        # 边界条件：s长度为1 直接返回
        result = {}

        for i in range(len(s)):
            # 以 i 为起点，启动扩散
            r = ""
            k = 0
            j = 0
            # 边界处理，提前处理i+1，放置越界
            if i + 1 >= len(s):
                continue

            # 情况1，回文串的字符数量为 even Vi = Vi+1
            # j为左移
            # k为右移
            # 循环满足：j在左边界内 且 k在右边界内，且j、k值相等，则同时移动j、k，将左字符加入result左侧，右字符加入result右侧
            # 跳出循环后：记录hash，key为回文长度，v为回文string
            if s[i] == s[i + 1]:
                j = i
                k = i + 1
                while j >= 0 and k < len(s) and s[j] == s[k]:
                    r = s[j] + r
                    r += s[k]
                    j -= 1
                    k += 1
            # 记录结果
            if r:
                result.update({len(r): r})
            # 情况2，回文串字符数量是 odd Vi-1 = Vi+1，且不越界
            # j为左移
            # k为右移动
            # 循环满足：j、k不越界的情况下，j、k相等，则同时移动j、k，将左字符加入result左侧，右字符加入result右侧
            # 跳出循环后：记录hash，key为回文长度，v为回文string
            if i - 1 >= 0 and i + 1 < len(s) and s[i - 1] == s[i + 1]:
                r = s[i]
                j = i - 1
                k = i + 1
                while j >= 0 and k < len(s) and s[j] == s[k]:
                    r = s[j] + r
                    r += s[k]
                    j -= 1
                    k += 1
            if r:
                result.update({len(r): r})

        print(result)
        # 输出结果
        if result:
            return result[max(result.keys())]
        elif s:
            return s[0]
        else:
            return ""
