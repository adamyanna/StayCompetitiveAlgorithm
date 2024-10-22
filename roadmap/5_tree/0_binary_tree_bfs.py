#!/usr/bin/env python3

# BFS - Breadth First Search
# 二叉树分为两种不同类型的遍历方式
# 二叉树的DFS BFS
# 1. BFS - Breadth First Search
#       - 优先从上到下遍历每一层的节点
#       - 想象一个为：top层1，第二层2、3，bottom层4、5、6、7的二叉树
#       - 广度优先的输出结果就应该是：根部、左叶子、右叶子节点，1、2、3、4、5、6、7，从上到下遍历
# * 方法：
#   1. 初始化一个queue，并将root入queue
#   2. 对queue使用while循环
#   3. 循环中pop queue第一个元素，值为二叉树节点值
#   4. 从L - R 的顺序将pop出的节点的左右叶子节点append 入Queue
#   5. queue为空，遍历结束
# BFS: 广度优先搜索遍历 iteration

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):

    def btree_bfs(self, root):
        result = [] # output all value
        queue_l = [root]
        while queue_l:
            # pop出当前的队列首个元素
            node = queue_l.pop(0)
            result.append([node.val][:][0])
            if node.left:
                queue_l.append(node.left)
            if node.right:
                queue_l.append(node.right)
            if not queue_l:
                return node.val