#!/usr/bin/env python3

"""
path-sum

输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
"""


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree_from_array(array):
    import queue
    def bfs_construct(a):
        if not a or not a[0]: return None
        root = TreeNode(a[0])
        q = queue.Queue()
        q.put(root)
        index = 1
        while index < len(a) and not q.empty():
            node = q.get()
            if a[index] and a[index] != "null":
                node.left = TreeNode(a[index])
                q.put(node.left)
            else:
                node.left = None
            index += 1
            if index < len(a) and a[index] and a[index] != "null":
                node.right = TreeNode(a[index])
                q.put(node.right)
            else:
                node.right = None
            index += 1

        return root

    return bfs_construct(array)


class Solution(object):
    def search_path_sum(self, root, target):

        has_sum = []
        def recur(node, result):
            if node:
                result += node.val
            else:
                return
            if node.left is None and node.right is None:
                if result == target:
                    has_sum.append(True)
                    return
                result -= node.val
            recur(node.left, result)
            recur(node.right, result)
        recur(root, 0)
        return len(has_sum) > 0


if __name__ == '__main__':
    root = construct_tree_from_array([5, 4, 8, 11, "null", 13, 4, 7, 2, "null", "null", "null", 1])
    s = Solution()
    print(s.search_path_sum(root, 22))
