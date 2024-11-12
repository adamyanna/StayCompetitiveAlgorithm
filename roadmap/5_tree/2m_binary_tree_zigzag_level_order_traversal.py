#!/usr/bin/env python3

"""
        3
    9       20
null null 15  7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
"""
import queue


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def array_to_b_tree(self, array):
        """
        BFS
        :param array:
        :return:
        """
        if array[0] == "null" or not array[0]:
            return None
        root = TreeNode(array[0])
        q = queue.Queue()
        q.put(root)
        index = 1
        while index < len(array) and not q.empty():
            node = q.get()
            if array[index] == "null" or not array[index]:
                node.left = None
            else:
                node.left = TreeNode(array[index])
                q.put(node.left)
            index += 1
            if index < len(array):
                if array[index] == "null" or not array[index]:
                    node.right = None
                else:
                    node.right = TreeNode(array[index])
                    q.put(node.right)
                index += 1

        return root

    def zigzag_level_order(self, root: TreeNode) -> list[list[int]]:
        """
                3
            9       20
        null null 15  7

        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[20,9],[15,7]]
        :param root:
        :return:
        """
        if not root: return []

        q = queue.Queue()
        q.put(root)
        result = []
        level_result = []
        next_n_count, cache_n_count = 0, 0
        last_n_count = 0
        while not q.empty():
            node = q.get()
            level_result.append(node.val)
            # handle left
            if node.left is not None:
                q.put(node.left)
            else:
                next_n_count += 1
            # handle right
            if node.right is not None:
                q.put(node.right)
            else:
                next_n_count += 1
            # condition for current level ending
            if len(level_result) == 2 ** len(result) - (last_n_count * 2 + cache_n_count):
                last_n_count = last_n_count * 2 + cache_n_count
                cache_n_count = next_n_count
                next_n_count = 0
                # handle result
                if len(result) % 2 == 0:
                    result.append(level_result[:])
                else:
                    level_result.reverse()
                    result.append(level_result[:])
                level_result = []

        return result


if __name__ == '__main__':
    """
            3
        9       20
    null null 15  7
    """
    s = Solution()
    root = s.array_to_b_tree([3,9,20,"null","null",15,7])
    print(s.zigzag_level_order(root))

    """
            1
        2       3
    4 null  null  5
    """
    root2 = s.array_to_b_tree([1,2,3,4,"null","null",5])
    print(s.zigzag_level_order(root2))










