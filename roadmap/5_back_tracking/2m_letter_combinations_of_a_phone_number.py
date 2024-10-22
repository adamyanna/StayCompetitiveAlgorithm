#!/usr/bin/env python3

## Letter Combinations of a Phone Number
"""
* 递归 + 深度优先
* 回溯 = 退回到原状态的方法
* 定义一个回退函数：确定如何回退&回退的时间点
* 一个条件达成回退：当前搜索深度已到达数组末尾
* 每一次状态更新（完成一次轮询），都需要更新状态，回退到上一个状态
"""

# Letter Combinations of a Phone Number
# 电话号码的字母组合

class Solution:
    def letterCombinations(self, digits: str):
        # 边界处理
        if not digits:
            return list()
        # 定义所有按键的字符组合
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # 同时在学习一次全排列
        # 递归 + 深度优先
        # 回溯 = 退回到原状态的方法

        # 定义一个回退函数：确定如何回退&回退的时间点
        # 一个条件达成回退：当前搜索深度已到达数组末尾
        # 未到达数组末尾之前，需要回溯全部

        i = 0 # 回溯从0开始
        result = []
        result_com = []
        def search(index):
            # return
            if index == len(digits):
                result.append("".join(result_com)) # 组合为string，并添加到结果
            # get all char
            c = phoneMap[index]
            for each_c in c:
                result_com.append(each_c)
                index += 1
                search(index)
                # example1：
                # 生成第一个结果，最后一位数字的第一个字母在此处返回
                # 回退到前一个状态以便更新新的字符
                # example2:
                # 最后一位数字所有的结果生成后，倒数第二个数字会在此处返回（深度遍历完成）
                # 回退到前一个状态以便更新新的字符
                # 结论：需要在此处pop出最后一个元素
                result_com.pop(-1) # 如何回退是回溯的精髓，什么时候回退
        search(index=i)


        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations