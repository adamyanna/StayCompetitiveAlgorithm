#!/usr/bin/env python3

"""
flatten-binary-tree-to-linked-list

给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
"""

"""
        1
       / \
      2   5
     / \   \
    3   4   6
    
        1
       / \
      2   5
       \   \
        3   6
         \
          4
    
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
"""


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
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
        else:
            node.left = None
        index += 1

        if index < len(array):
            if array[index] and array[index] != n:
                node.right = TreeNode(array[index])
                q.put(node.right)
            else:
                node.right = None
            index += 1

    return root


class Solution(object):
    def flatten(self, root):
        """
                1
               / \
              2   5
             / \   \
            3   4   6

                1
               / \
              2   5
               \   \
                3   6
                 \
                  4
        :param root:
        :return:
        """

        self.last_right = None
        def dfs(node):
            if not node: return None
            dfs(node.right)
            dfs(node.left)
            node.right = self.last_right
            node.left = None
            self.last_right = node

        dfs(root)
        return root

if __name__ == '__main__':
    root = deserialize_array_to_tree([1,2,5,3,4,"null",6])
    s = Solution()
    new_root = s.flatten(root)
    print(new_root.val)