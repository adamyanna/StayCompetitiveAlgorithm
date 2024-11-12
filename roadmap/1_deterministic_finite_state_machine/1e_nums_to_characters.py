#!/usr/bin/env python3

class Solution(object):
    def convert_num_to_string(self, nums):

        result = ""

        hash = {}
        for i in range(26):
            hash[i+1] = chr(i+ord("a"))

        i = 0
        while i < len(nums):
            # 24#2
            if int(nums[i]) == 1 or int(nums[i]) == 2:
                if i + 2 < len(nums) and nums[i + 2] == "#":
                    temp = int(nums[i]) * 10 + int(nums[i+1])
                    if not 0 <= temp <= 26:
                        i += 3
                        continue
                    result += hash[int(nums[i]) * 10 + int(nums[i+1])]
                    i += 3
                    continue
            result += hash[int(nums[i])]
            i += 1

        return result

"""
Integer to characters
有限状态自动机 - 求解
分析
1. 转换规则编写子函数
2. 
自动机的实现
确定性有限状态自动机 Deterministic Finite State Machine/Automaton
Automaton 状态定义
--------- | 1-26 | #    | not 1-26 | end |
start     | char | cache | jump | end
char      | char | cache | jump | end
cache      | char | cache | jump | end
jump      | char | jump | jump | end
end       | end | end | end | end
"""

class SolutionAutomaton(object):

    def __init__(self):
        self.state = "start"
        self.table = {
            "start": ["char", "cache", "jump", "end"],
            "char": ["char", "cache", "jump", "end"],
            "cache": ["char", "cache", "jump", "end"],
            "jump": ["char", "jump", "jump", "end"],
            "end": ["end", "end", "end", "end"],
        }

        self.cache = 0
        self.start_num = ord("a")
        self.result = ""

    def get_col(self, num=0, get_cache=False):
        if 0 <= num <= 26:
            if get_cache: return 1
            return 0
        elif num > 26:
            return 2
        return 3

    def get(self, num_char):
        if num_char == "#":
            col = self.get_col(num=self.cache, get_cache=True)
        else:
            # update cache
            num = int(num_char)
            if 0 < self.cache <= 9:
                self.cache = self.cache * 10 + num
            else:
                self.cache = self.cache % 10 * 10 + num
            col = self.get_col(num=num)
        self.state = self.table[self.state][col]
        if self.state == "char":
            self.result += chr(num - 1 + self.start_num)
        elif self.state == "cache":
            self.result = self.result[:-2]
            self.result += chr(self.cache - 1 + self.start_num)
        elif self.state == "jump":
            self.result = self.result[:-2]



if __name__ == '__main__':


    s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#27#28#29"
    auto = SolutionAutomaton()
    for v in s:
        auto.get(v)
    print(Solution().convert_num_to_string(nums=s) == auto.result)
