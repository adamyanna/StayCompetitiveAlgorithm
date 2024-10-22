# Group Anagrams
# method1: sort 每一个单词，将结果作为 hash key，将单词作为 hash list value，最终将hash value 转换为 list
# method2: 相同的字符出现的次数一定是一致的，生成一个26个字母的数组 key_list = [0] # 26, 通过 ord(ch) - ord("a")
# 获取每个字符在26个字母中顺序的整形，作为 index 对多次出现在 key_list中的结果 +1，将key转换为 string，作为 hash的key，
# 将单词作为 hash list value的值，即可得到最终结果

class Solution(object):
    def groupAnagrams(self, strs):
        if strs is None:
            return []
        result = dict()
        for v_str in strs:
            key_list = [0] * 26
            for v_char in v_str:
                index = ord(v_char) - ord("a")
                key_list[index] += 1
            key = "".join([str(v) for v in key_list])
            if key not in result:
                result[key] = []
            result[key].append(v_str)
        return list(result.values())

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(Solution().groupAnagrams(["a"]))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams([]))
    print(Solution().groupAnagrams(None))



