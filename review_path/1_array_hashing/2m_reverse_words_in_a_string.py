#!/usr/bin/env python3

# Reverse Words in a String
# 翻转字符串里的单词，结果是从后向前读单词的string
# strip 、 split、 反向读取 List，然后空格join为string

# 原地算法，双指针 - 仅适用于当前字符串内都是单空格的情况， 多空格难以处理
# 双空格标记法

class Solution(object):
    def reverseWordsInAString(self, input_str):
        # "this is a string"
        # -> "string a is this"
        # double pointers
        # 原地算法
        # space: O(1)
        # time: O(n)
        input_str = input_str.strip()
        l_start = l = 0
        r_end = r = len(input_str) - 1
        r_word = l_word = ""
        while l <= r:
            if input_str[l] != " ":
                l += 1
            elif input_str[l] == " " and l > 0 and input_str[l-1] == " ":
                l += 1
            else:
                l_word = input_str[l_start:l]
                l_word = l_word.strip()
            if input_str[r] != " ":
                r -= 1
            elif input_str[r] == " " and 0 < r < (len(input_str) - 2) and input_str[r+1] == " ":
                r -= 1
            else:
                r_word = input_str[r+1:r_end+1]
                r_word = r_word.strip()
            if len(l_word) > 0 and len(r_word) > 0:
                # "string is a this"
                print("<%s>" % r_word)
                print("<%s>" % l_word)
                str_left_part = input_str[:l_start].strip() + " " + r_word
                str_right_part = l_word + " " + input_str[r_end+1:].strip()

                if input_str[l:r+1] == " ":
                    input_str = str_left_part + " " + str_right_part
                elif len(input_str[l:r+1].strip()) > 0:
                    input_str = str_left_part + " " + input_str[l:r+1].strip() + " " + str_right_part
                else:
                    input_str = str_left_part + str_right_part

                if l == r: break
                l = l_start = len(str_left_part) + 1
                r = r_end = len(input_str) - 1 - len(str_right_part) - 1
                r_word = l_word = ""
            print("<%s>" % input_str)

        return input_str.strip()

if __name__ == '__main__':
    print("<%s>" % Solution().reverseWordsInAString("sasdf   tasdf aasdf "))