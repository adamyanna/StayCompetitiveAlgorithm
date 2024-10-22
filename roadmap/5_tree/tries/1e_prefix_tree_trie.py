#!/usr/bin/env python3

# 前缀树
# 1. 多叉树
# 2. 从root开始，支持插入、搜索
# 3. 如果字符串起始字符不在root则重新开始插入，如果存在则继续向下寻找
# 4. 实现方式是在class内实现一个类似链表的结构，链表的值存储所有的26个字母从0开始的index，该节点所有的值，就代表上一个节点所有的叶子
# [0...25] -> [0...25] -> [0...25]
# search a string
# insert a string
# search a string's prefix
# start with a string's prefix

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None