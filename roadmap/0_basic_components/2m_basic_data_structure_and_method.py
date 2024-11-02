#!/usr/bin/env python3

"""
High Occurrence of Algorithm problem pattern

1. Array & Hash
2. Recursion [Backtracking]
3. DFS & BFS
4. Binary Search
5. Sliding Window
6. Heap
"""

"""
6
Understand Basic Data Structure of Python
Heap & Queue
"""

import heapq
import queue


class Solution6(object):
    def heap_review(self, unsorted_array):
        heap_list = []
        for v in unsorted_array:
            heapq.heappush(heap_list, v)
        for _ in range(len(heap_list)):
            print(heapq.heappop(heap_list))
        print(heap_list)

    def queue_review(self, unsorted_array):
        self.this_queue = queue.Queue()
        for v in unsorted_array:
            self.this_queue.put(v)
        while not self.this_queue.empty():
            print(self.this_queue.get())


"""
5
Sliding Window
"""

class SlidingWindowPractice(object):
    def find_longest_sub_string_length(self, input_string):

        non_replication_char = set()
        r, result = -1, 0

        for l in range(len(input_string)):
            # 2. moving l & remove last l from set
            if 0 < l:
                non_replication_char.remove(input_string[l-1])
            # 1. moving r to last non repeat char & save to set
            while r + 1 < len(input_string) and input_string[r+1] not in non_replication_char:
                non_replication_char.add(input_string[r+1])
                r += 1

            result = max(result, r - l)

        return result



class Solution5(object):
    def sliding_window_review(self):
        pass


"""
4
Binary Search
"""

class Solution3(object):
    def binary_search_review(self, sorted_array, target):
        """
        :param sorted_array:
        :param target:
        :return: Boolean
        """

        l, r = 0, len(sorted_array)
        while l < r:
            m = (l + r) // 2
            if sorted_array[m] < target:
                l = m + 1
            else:
                r = m

        if 0 <= l < len(sorted_array):
            if sorted_array[l] == target:
                return True
        return False

"""
3
BFS & DFS
Binary Tree
Graph
"""
import queue
class BTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution3(object):
    """
    1. deserialize a string to a binary tree
    2. bfs to tree
    3. pre dfs to tree
    4. mid dfs to tree
    5. post dfs to tree
    6. serialize tree back to original string
        - dfs
            - pre
            - mid
            - post
        - bfs
    """
    def deserialize_string_to_b_tree(self, s_string):

        iter_array = iter(s_string.split(","))

        def deserializer():
            value = next(iter_array)
            if value == "null":
                return None
            return BTreeNode(value, left=deserializer(), right=deserializer())

        return deserializer()

    def bfs(self, root):
        bfs_result = []
        tree_queue = queue.Queue()
        tree_queue.put(root)
        while not tree_queue.empty():
            node = tree_queue.get()
            if node is None:
                continue
            bfs_result.append(node.value)
            tree_queue.put(node.left)
            tree_queue.put(node.right)

        return bfs_result

    def dfs_pre_oder(self, root):
        dfs_result = []
        def recur(node):
            if node is None: return
            dfs_result.append(node.value)
            recur(node.left)
            recur(node.right)

        recur(root)
        return dfs_result

    def dfs_mid_order(self, root):
        dfs_result = []
        def recur(node):
            if node is None: return
            recur(node.left)
            dfs_result.append(node.value)
            recur(node.right)

        recur(root)
        return dfs_result

    def dfs_post_order(self, root):
        dfs_result = []

        def recur(node):
            if node is None: return
            recur(node.left)
            recur(node.right)
            dfs_result.append(node.value)

        recur(root)
        return dfs_result

    def serialize_b_tree_to_string(self, root, order="pre"):

        def serializer(node, s_string):
            if node is None:
                s_string += "null,"
            else:
                s_string += node.value + "," + serializer(node.left, s_string) + serializer(node.right, s_string)
            return s_string


        def serializer_mid(node, s_string):
            if node is None:
                s_string += "null,"
            else:
                s_string += serializer_mid(node.left, s_string) + node.value + "," + serializer_mid(node.right, s_string)
            return s_string

        def serializer_post(node, s_string):
            if node is None:
                s_string += "null,"
            else:
                s_string += serializer_post(node.left, s_string) + serializer_post(node.right, s_string) + node.value + ","
            return s_string

        if order == "pre":
            return serializer(root, "")
        elif order == "mid":
            return serializer_mid(root, "")
        elif order == "post":
            return serializer_post(root, "")

        return serializer(root, "")

    def serializer_b_tree_to_string_with_bfs(self, root):
        result_s_string = ""
        b_tree_queue = queue.Queue()
        b_tree_queue.put(root)
        while not b_tree_queue.empty():
            node = b_tree_queue.get()
            if node is None:
                result_s_string += "null,"
                continue
            result_s_string += node.value + ","
            b_tree_queue.put(node.left)
            b_tree_queue.put(node.right)

        return result_s_string


    ########
    # Graphs
    ########

    GRAPH = {
        'A': ['B', 'F'],
        'B': ['C', 'I', 'G'],
        'C': ['B', 'I', 'D'],
        'D': ['C', 'I', 'G', 'H', 'E'],
        'E': ['D', 'H', 'F'],
        'F': ['A', 'G', 'E'],
        'G': ['B', 'F', 'H', 'D'],
        'H': ['G', 'D', 'E'],
        'I': ['B', 'C', 'D'],
    }

    def dfs_graph(self, graph):
        result = []
        dfs_searched = set()
        def recur(node):
            if node not in dfs_searched:
                dfs_searched.add(node)
                result.append(node)
            for vector in graph[node]:
                if vector not in dfs_searched:
                    recur(vector)

        recur([k for k in graph.keys()][0])
        return result

    def bfs_graph(self, graph, start):
        result = []
        bfs_searched = set()
        g_queue = queue.Queue()
        g_queue.put(start)
        while not g_queue.empty():
            vector = g_queue.get()
            if vector not in bfs_searched:
                bfs_searched.add(vector)
                result.append(vector)
                for vector_v in graph[vector]:
                    g_queue.put(vector_v)

        return result

class GraphSolution(object):
    GRAPH = {
        'A': ['B', 'F'],
        'B': ['C', 'I', 'G'],
        'C': ['B', 'I', 'D'],
        'D': ['C', 'I', 'G', 'H', 'E'],
        'E': ['D', 'H', 'F'],
        'F': ['A', 'G', 'E'],
        'G': ['B', 'F', 'H', 'D'],
        'H': ['G', 'D', 'E'],
        'I': ['B', 'C', 'D'],
    }
    START_VECTOR = "A"
    def bfs(self, graph, start_v):
        searched = set()
        result = []
        g_queue = queue.Queue()
        g_queue.put(start_v)
        while not g_queue.empty():
            vector = g_queue.get()
            if vector not in searched:
                searched.add(vector)
                result.append(vector)
                for v in graph[vector]:
                    g_queue.put(v)
        return result


    def dfs(self, graph, start_v):
        searched = set()
        result = []
        def recur(vector):
            if vector not in searched:
                searched.add(vector)
                result.append(vector)
            for v in graph[vector]:
                if v not in searched:
                    recur(v)
        recur(start_v)
        return result


"""
2
Recursion
Backtracking
"""

class PermutationsSolution(object):

    def permutation1(self, nums):

        result = []
        def recur(start_point=0):
            if start_point == len(nums):
                result.append(nums[:])

            for i in range(start_point, len(nums)):
                # recursive switch from the startpoint
                nums[start_point], nums[i] = nums[i], nums[start_point]
                # updating startpoint
                recur(start_point=start_point+1)
                # back to original state
                nums[i], nums[start_point] = nums[start_point], nums[i]

                # 1 23 -> 123 [switch on its own index for first result, back tracking to original]
                # 1 32 -> 123 [0 no change, 1 & 2 switch, back to origin]
                # 2 13 -> 213 [0 1 switch]
                # 231 -> 213 -> 123 [1, 2 switch, back to last origin & back to origin]
                # 321 -> 321 [0, 3 switch]
                # 312 -> 321 -> 123 [1, 2 switch, back to last origin & back to origin]

        recur()
        return result


    def permutation2(self, nums):
        result = []
        def recur(start_index=0):
            if start_index == len(nums):
                result.append(nums[:])
            replication = set()
            for i in range(start_index, len(nums)):
                if nums[i] in replication:
                    continue
                replication.add(nums[i])
                # switch
                nums[start_index], nums[i] = nums[i], nums[start_index]
                recur(start_index=start_index+1)
                nums[i], nums[start_index] = nums[start_index], nums[i]

        recur()
        return result




"""
main test
"""

if __name__ == '__main__':
    #       1
    #   2     3
    #       4   5
    s = Solution3()
    root = s.deserialize_string_to_b_tree("1,2,null,null,3,4,null,null,5,null,null")
    # do bfs to root
    print("bfs: ", s.bfs(root))
    # do pre dfs
    print("dfs pre: ", s.dfs_pre_oder(root))
    # do mid dfs
    print("dfs mid: ", s.dfs_mid_order(root))
    # do post dfs
    print("dfs post: ", s.dfs_post_order(root))

    # serialize back to string
    print(s.serialize_b_tree_to_string(root, "pre"))
    print(s.serialize_b_tree_to_string(root, "mid"))
    print(s.serialize_b_tree_to_string(root, "post"))

    # serialize back to string with bfs
    print(s.serializer_b_tree_to_string_with_bfs(root))


    # Graph
    print(s.dfs_graph(Solution3.GRAPH))
    start = "A"
    print(s.bfs_graph(Solution3.GRAPH, start))


    # Graph bfs
    print(GraphSolution().bfs(GraphSolution.GRAPH, GraphSolution.START_VECTOR))
    # Graph dfs
    print(GraphSolution().dfs(GraphSolution.GRAPH, GraphSolution.START_VECTOR))


    # backtracking permutations
    print(PermutationsSolution().permutation1([1,2,3]))
    print(PermutationsSolution().permutation2([1,2,2,3]))


    # Sliding window
    print(SlidingWindowPractice().find_longest_sub_string_length("abccabcd"))