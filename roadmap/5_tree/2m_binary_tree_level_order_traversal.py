#!/usr/bin/env python3


import queue


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def array_to_tree_dfs_pre_order(self, array):
        iter_array = iter(array)

        def array_to_tree():
            v = next(iter_array)
            if not v or v == "null":
                return None
            return TreeNode(v, left=array_to_tree(), right=array_to_tree())

        return array_to_tree()

    def array_to_tree_dfs_pre_order_2(self, array):
        """
        MARK - Bad Practice
        :param array:
        :return:
        """
        def handler(a):
            if not a:
                return None
            if not a[0] or a[0] == "null":
                return None
            node = TreeNode(a.pop(0))
            node.left = handler(a[1:])
            node.right = handler(a[2:])
            return node

        return handler(array)

    def test_dfs_pre_order(self, root):
        result = []
        def dfs(root):
            if root is None: return None
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        return result

    def array_to_tree_bfs(self, array):

        if array[0] == "null":
            return None

        root = TreeNode(array[0])
        q = queue.Queue()
        q.put(root)

        index = 1
        while index < len(array) and not q.empty():
            # get node
            node = q.get()
            # handle left
            if array[index] != "null":
                node.left = TreeNode(array[index])
                q.put(node.left)
            else:
                node.left = None
            index += 1
            # handle right
            if index < len(array):
                if array[index] != "null":
                    node.right = TreeNode(array[index])
                    q.put(node.right)
                else:
                    node.right = None
                index += 1

        return root

    def bfs_b_tree(self, root: TreeNode):
        """
        tree
            1
          2   3
        null null    6        7
                  null null 10 11
        size[0] = 1
        size[1] = 2
        size[2] = 4 - 2
        size[3] = 8 - 2 * 2 - 2
        result.size = level ** 2 - last_null * 2 - level_null

        :param root:
        :return:
        """
        result = []
        current_level_result = []
        q = queue.Queue()
        q.put(root)

        next_null, cache_null = 0, 0
        last_null = 0

        while not q.empty():
            node = q.get()
            # update val
            if node:
                current_level_result.append(node.val)

            if node.left:
                q.put(node.left)
            else:
                next_null += 1
            if node.right:
                q.put(node.right)
            else:
                next_null += 1

            if len(current_level_result) == 2 ** len(result) - (last_null * 2 + cache_null):
                last_null = last_null * 2 + cache_null
                cache_null = next_null
                next_null = 0
                # update result for every level
                result.append(current_level_result[:])
                current_level_result = []

        return result


if __name__ == '__main__':
    s = Solution()
    root = s.array_to_tree_dfs_pre_order([3,9,"null","null",20,15,"null","null",7,1,"null","null",2,"null","null"])
    print(Solution().bfs_b_tree(root))

    root4 = s.array_to_tree_dfs_pre_order([1,2,"null","null","null"])
    print(Solution().bfs_b_tree(root4))

    """
        1
     2    3
    4 5  6 7
    """

    # root1 = s.array_to_tree_bfs([1,2,3,4,5,6,7])
    # print(s.bfs_b_tree(root1))
    # print(s.test_dfs_pre_order(root1))
    #
    # root2 = s.array_to_tree_dfs_pre_order_2([1,2,4,5,3,6,7])
    # print(s.test_dfs_pre_order(root2))
    #
    # root3 = s.array_to_tree_dfs_pre_order([1,2,4,"null","null",5,"null","null",3,6,"null","null",7,"null","null"])
    # print(s.test_dfs_pre_order(root3))
