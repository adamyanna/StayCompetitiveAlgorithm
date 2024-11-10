#!/usr/bin/env python3

"""
binary-tree-maximum-path-sum/description/

输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import queue
def deserialize_array_to_tree(array):
    n = "null"
    if not array or not array[0] or array[0] == n:
        return None
    root = TreeNode(array[0])
    q = queue.Queue()
    q.put(root)
    index = 1
    while index < len(array) and not q.empty():
        node = q.get()
        if array[index] and array[index] != n:
            node.left = TreeNode(array[index])
            q.put(node.left)
        index += 1
        if index < len(array):
            if array[index] and array[index] != n:
                node.right = TreeNode(array[index])
                q.put(node.right)
            index += 1

    return root

class Solution(object):
    def max_path_sum(self, root):
        """
                -10
                9 20
        null,null   15,7
        分析：
        递归 recursive
        1. 左右子树做递归操作，返回 node 和左右子树中最大值的路径，回溯到上一层，作为路径的一部分
        2. 将回溯左右子树结果与当前 node.val 相加，对比当前最大结果，取最大值
        :param root:
        :return:
        """
        import sys
        self.result = -(sys.maxsize + 1)

        def recur(node):
            if not node: return 0

            left_sub_tree_max = max(recur(node.left), 0)
            right_sub_tree_max = max(recur(node.right), 0)

            new_path = node.val + left_sub_tree_max + right_sub_tree_max
            self.result = max(self.result, new_path)

            return node.val + max(left_sub_tree_max, right_sub_tree_max) # backtracking to previous node as top


        recur(root)
        return self.result


if __name__ == '__main__':
    root = deserialize_array_to_tree([-10,9,20,"null","null",15,7])
    s = Solution()
    print(s.max_path_sum(root))