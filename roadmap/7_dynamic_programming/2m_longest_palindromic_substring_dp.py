#!/usr/bin/env python3

# Longest Palindromic Substring 回文 - 动态规划
"""
初始化 dp 方程：dp[i][j] = F
  - dp 在 i dao j 的区间内是否是回文
  - 遍历从2 到 n 的所有可能长度的回文串
状态转移：
  - dp[i][j] = dp[i + 1][j - 1]
  - 当 i+1 到 j-1 不是回文，那么i到j也不是
  - 当 i值j 相等，i+1 到 j-1 是回文，那么i到j也是
"""


# TODO
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
