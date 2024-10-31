#!/usr/bin/env python3

## Serialize and Deserialize Binary Tree
"""
* BT 的 DFS、BFS
* BT serialize & deserialize
* 二叉树的序列化，直接先用 DFS-pre_oder 即可，pre_oder中将val转换为string并add
* 反序列化要注意，同样使用 DFS-pre_oder，在 pre_oder 中将转化为数组的输入的首个元素pop出数组，
    并将其赋值给新创建的节点，再将数组递归调用给节点的左右叶子
* 反序列化，需要考虑边界条件，队首元素为空的情况下，直接返回None
"""

# Serialize and Deserialize Binary Tree
#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # 深度遍历
    # 不使用静态变量 使用递归
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def recursive_serializer(node, string):
            if node is None:
                string += "None,"
            else:
                string += str(node.val) + ","
                string = recursive_serializer(node.left, string)
                string = recursive_serializer(node.right, string)
            return string

        return recursive_serializer(root, '')

    # 反序列化，将数组转化成二叉树
    # 使用了递归实现了序列化，侧同理反序列化也使用递归
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def recursive_serializer(data):
            if data[0] == "None":
                data.pop(0)
                return None

            node = TreeNode(data[0])
            data.pop(0)
            node.left = recursive_serializer(data)
            node.right = recursive_serializer(data)
            return node

        return recursive_serializer(data.split(','))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

if __name__ == '__main__':
    # "1,2,3,null,null,4,5"
    #         1
    #     2       3
    # null null 4  5
    root = TreeNode("1")
    root.left = TreeNode("2")
    root.right = TreeNode("3")
    root.right.left = TreeNode("4")
    root.right.right = TreeNode("5")

    codec = Codec()
    print(codec.serialize(root))
    result = codec.deserialize(codec.serialize(root))
    print("finish")

