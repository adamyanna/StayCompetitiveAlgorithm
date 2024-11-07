#!/usr/bin/env python3

"""
construct-binary-tree-from-inorder-and-postorder-traversal

输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder 和 postorder 都由 不同 的值组成
postorder 中每一个值都在 inorder 中
inorder 保证是树的中序遍历
postorder 保证是树的后序遍历
"""

"""
        3
    9       20
null null 15 7

inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]

解法，从后序遍历中的末尾元素可以找到第一个根结点，找到该节点在中序遍历中的位置
此时该位置前的元素为left，后面的元素为right
递归继续对前后两个孩子进行同样操作
"""

class TreeNode(object):
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def build_tree(self, mid_order, post_order):
        # all order construct by different nums
        min_order_map = {v:k for k, v in enumerate(mid_order)}
        def recur(l, r):
            if l > r or not post_order: return None
            val = post_order.pop()
            node_index = min_order_map[val]
            return TreeNode(val, recur(node_index+1, r), recur(l, node_index-1))

        return recur(0, len(post_order) -1)

    def dfs_pre(self, root):
        result = []
        def recur(node):
            if not node:
                result.append(None)
                return None
            result.append(node.val)
            recur(node.left)
            recur(node.right)

        recur(root)
        return result

    def bfs(self, root):
        import queue
        q = queue.Queue()
        q.put(root)
        result = []
        while not q.empty():
            node = q.get()
            if node:
                result.append(node.val)
                q.put(node.left)
                q.put(node.right)
            else:
                result.append(None)

        return result


if __name__ == '__main__':
    """
            3
        9       20
    null null 15 7
    """
    s = Solution()
    root = s.build_tree([9,3,15,20,7], [9,15,7,20,3])
    print(s.dfs_pre(root))
    print(s.bfs(root))

