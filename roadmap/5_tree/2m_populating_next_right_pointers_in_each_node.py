#!/usr/bin/env python3

"""
populating-next-right-pointers-in-each-node/

##########
<<EOF
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
EOF
##########

输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import queue
def deserialize_array_to_b_tree(array):
    n = "null"
    if not array or not array[0] or array[0] == n:
        return None
    root = Node(array[0])
    q = queue.Queue()
    q.put(root)
    index = 1
    while index < len(array) and not q.empty():
        node = q.get()
        if array[index] and array[index] != n:
            node.left = Node(array[index])
            q.put(node.left)
        index += 1
        if index < len(array):
            if array[index] and array[index] != n:
                node.right = Node(array[index])
                q.put(node.right)
            index += 1

    return root

class Solution(object):
    def connect(self, root: Node):
        """
        1,
        2,3,
        4,5,6,7
        :param root:
        :return:
        """
        if not root: return root
        self.cache_node = root
        current_level = 0
        current_level_count = 0
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if not node:
                continue
            current_level_count += 1
            if not self.cache_node:
                self.cache_node = node
            else:
                if current_level_count < 2 ** current_level:
                    self.cache_node.next = node
                    self.cache_node = node
                else:
                    current_level += 1
                    current_level_count = 0
                    self.cache_node.next = node
                    node.next = None
                    self.cache_node = None

            q.put(node.left)
            q.put(node.right)
        return root

if __name__ == '__main__':
    root = deserialize_array_to_b_tree([1,2,3,4,5,6,7])
    s = Solution()
    s.connect(root)
    print(root)