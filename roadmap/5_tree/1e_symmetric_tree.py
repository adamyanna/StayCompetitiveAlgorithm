#!/usr/bin/env python3
# symmetric-tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def isSymmetric(self, root):

        if root is None: return False
        def is_mirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (is_mirror(t1.left, t2.right) and
                    is_mirror(t1.right, t2.left) and
                    (t1.val == t2.val))

        return is_mirror(root.left, root.right)

