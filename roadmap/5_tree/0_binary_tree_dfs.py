#!/usr/bin/env python3

# DFS - Depth First Search
# 二叉树分为两种不同类型的遍历方式
# 二叉树的DFS BFS
#        1
#   2        3
# 4   5    6   7
# 2. DFS - Depth First Search
#       - 深度优先的遍历方式
#       - 有先、中、后，三种方式，先、中、后都是用来表示root在深度优先中的顺序
#       - 想象一个为：top层1，第二层2、3，bottom层4、5、6、7的二叉树
#       - 先：1、2、4、5、3、6、7
#       - 中：4、2、5、1、6、3、7
#       - 后：4、5、2、6、7、3、1
# 通常使用递归实现 Recursive、Recursion
# pre_oder -> root-left-right
# mid_oder -> left-root-right
# post_oder -> left-right-root

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def btree_dfs(self, root):
        result = []

        def binary_tree_dfs(node):
            if node is not None:
                result.append(node.val)  # 优先存储根节点结果，pre_oder
                binary_tree_dfs(node.left)
                result.append(node.val)  # 优先存储左叶子节点结果，mid_oder
                binary_tree_dfs(node.right)
                result.append(node.val)  # 优先存储左、右叶子节点结果，post_oder
