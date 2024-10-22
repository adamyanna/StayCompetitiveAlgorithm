#!/usr/bin/env python3

# Longest Substring Without Repeating Characters
# 最长无重复字符子字符串，在一个字符串中找到最长的无任何字符重复的子串
# 用次题目复习dynamic programing
# 1. 起始位置 index0 开始 rptr 移动到最后一个不重复字符，并记录当前最大值
# 2. 使用 set 用来记录当前不重复字符
# 3. 条件 1 跳出后，移动 lptr 将其移动到下一个位置，并从 set 记录中踢出前一个重复字符
# 4. 直到最终l指针到达终点

## Longest Substring Without Repeating Characters
# * 最长无重复字符子字符串，在一个字符串中找到最长的无任何字符重复的子串

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # double ptr and slide window
        # 1. 起始位置 index0 开始 rptr 移动到最后一个不重复字符，并记录当前最大值
        # 2. 使用 set 用来记录当前不重复字符
        # 3. 条件 1 跳出后，移动 lptr 将其移动到下一个位置，并从 set 记录中踢出前一个重复字符
        # 4. 直到最终l指针到达终点

        # 0 init vars to store data
        no_repeat_c = set()  # save current value
        length = len(s)
        # left pointer start from index 0
        # right pointer start from index 1
        rptr, result = -1, 0
        # 1. move left pointer
        for lptr in range(0, length):
            # 3. remove previous left pointer value from set, and get a new result from right pointer movement
            if 0 < lptr < length:
                no_repeat_c.remove(s[lptr - 1])
            # 2. move rptr to index+1, and check if index is valid and Character not in set
            while rptr + 1 < length and s[rptr + 1] not in no_repeat_c:
                no_repeat_c.add(s[rptr + 1])
                rptr += 1

            result = max(result, rptr - lptr)

        return result
