#!/usr/bin/env python3

"""
path-sum

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
"""

import queue


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize_array_to_tree(array):
    null = "null"
    if not array or not array[0] or array[0] == null:
        return None
    root = TreeNode(array[0])
    q = queue.Queue()
    q.put(root)
    index = 1
    while index < len(array) and not q.empty():
        node = q.get()
        if array[index] and array[index] != null:
            node.left = TreeNode(array[index])
            q.put(node.left)
        else:
            node.left = None
        index += 1
        if index < len(array):
            if array[index] and array[index] != null:
                node.right = TreeNode(array[index])
                q.put(node.right)
            else:
                node.right = None
            index += 1

    return root


class Solution(object):
    def path_sum(self, root, target):
        """
        1. get every node sum
        2. target = sum[left] - sum[node]

        Analyze:

        1. Use hash to save count of current prefix sum's count, default is 0:1 to count as 1 time
        2. Use current_recur_sum - target as to get count of occurrence of hash
        3. add up result to output

        {
            hash = {0:1}
            result += hash.get(current_sum - target, 0)

            hash[current_sum] += 1
            result += recur()
            result += recur()
            hash[current_sum] -= 1
        }

        :return:
        """
        sum_count_map = {0:1}

        def recur(node, curr_sum):
            if not node:
                return 0
            result = 0
            curr_sum += node.val
            result += sum_count_map.get(curr_sum - target, 0)

            # print(node.val, curr_sum)
            # print(curr_sum - target)
            # print(sum_count_map)
            # print("-------result:", result)
            sum_count_map[curr_sum] = sum_count_map.get(curr_sum, 0) + 1

            result += recur(node.left, curr_sum)
            result += recur(node.right, curr_sum)

            sum_count_map[curr_sum] -= 1

            return result

        return recur(root, 0)


if __name__ == '__main__':
    """
                    10
            5           -3
        3       2       null 11
    3   -2    null 1
    
    """
    root = deserialize_array_to_tree([10, 5, -3, 3, 2, "null", 11, 3, -2, "null", 1])

    s = Solution()
    print(s.path_sum(root, 8))


    """
              5
        4              8
      11    n        13  4
    7   2  n n      5 1
    """
    root2 = deserialize_array_to_tree([5,4,8,11,"null",13,4,7,2,"null","null",5,1])
    print(s.path_sum(root2, 22))
