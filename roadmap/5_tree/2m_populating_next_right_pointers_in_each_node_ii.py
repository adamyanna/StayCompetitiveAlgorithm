#!/usr/bin/env python3

"""
populating-next-right-pointers-in-each-node-ii

<<EOF
给定一个二叉树：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。

初始状态下，所有 next 指针都被设置为 NULL 。
EOF


输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import queue
def deserialize_array_to_tree(array):
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
    def connect(self, root: 'Node') -> 'Node':
        """
               1
             2   3
           4   5   7

        :param root:
        :return:
        """
        if not root: return root
        q = queue.Queue()
        q.put(root)
        current_level = 0
        current_level_count = 0

        next_level_null = 0
        current_level_null = 0

        last_node = root

        while not q.empty():
            node = q.get()
            if not node: continue

            if node.left:
                q.put(node.left)
            else:
                next_level_null += 1
            if node.right:
                q.put(node.right)
            else:
                next_level_null += 1

            current_level_count += 1
            if current_level_count + current_level_null < 2 ** current_level:
                if not last_node:
                    last_node = node
                    continue
                last_node.next = node
                last_node = node
            else:
                # current level end
                current_level += 1
                current_level_count = 0
                # update null count
                current_level_null = current_level_null * 2 + next_level_null
                next_level_null = 0
                if last_node: last_node.next = node
                node.next = None
                last_node = None
        return root


if __name__ == '__main__':
    """
            1
           2 N
          3 N
        4 N
       5
    """
    # root = deserialize_array_to_tree([1,2,None,3,None,4,None,5])
    root = deserialize_array_to_tree([1,2,3,4,5,None,7])
    s = Solution()
    s.connect(root)
    print(root)









