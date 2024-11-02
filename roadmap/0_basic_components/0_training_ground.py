# # # # # online coding
# # # #
# # # #
# # # # class Solution(object):
# # # #     def my_solution(self, input):
# # # #         # merge multiple sorted arrays
# # # #         # k 个数组
# # # #         # 1. k 每两个数组 merge， k/2，k/4
# # # #         # 2. binary 二分的方法
# # # #
# # # #         # edge case
# # # #
# # # #
# # # #         # input[0 - k]
# # # #         while len(input) > 1:
# # # #             array_a = input[0]
# # # #             array_b = input[len(input) - 1]
# # # #
# # # #             while len(array_a) > 0:
# # # #                 point = array_a[0]
# # # #                 # point = array_a[0] start from 0
# # # #                 l, r = 0, len(array_b) - 1
# # # #                 while l < r:
# # # #                     m = (l+r) // 2
# # # #                     m_value = array_b[m]
# # # #                     if m_value < point:
# # # #                         l = m + 1
# # # #                     elif m_value > point:
# # # #                         r = m - 1
# # # #                     else:
# # # #                         break
# # # #                     print("test l %d r %d" % (l, r))
# # # #                 if l == r:
# # # #                     m = l
# # # #                 # do merge
# # # #                 array_b.insert(m, point)
# # # #                 array_a.pop(0)
# # # #
# # # #             # update len
# # # #             input.pop(0)
# # # #         return input[0]
# # # #
# # #
# # #
# # # # language of chiose: Python
# # # # Algorithm: 1.1
# # # # class Solution(object):
# # # #     def get_sum_of_number(self, nums, target):
# # # #         """
# # # #         return two int or None
# # # #         """
# # # #         dp = {}
# # # #         for v in nums:
# # # #             result = target - v
# # # #             if v in dp:
# # # #                 return result, v
# # # #             dp[result] = v
# # # #
# # # #
# # # #         return None, None
# # #
# # #
# # # # 14:03 start
# # # # progamming
# # #
# # # class Solution(object):
# # #     # simulate_stack_with_two_queues
# # #     # use python list to simulate queue
# # #     # use list len to simulate return of queue size
# # #     # pop[0] remove element from queue head
# # #     # append add element from queue tail
# # #     # stack push 1,2,3
# # #     # queue a [1, 2, 3]
# # #     # queue b []
# # #     # pop -> first element = 3
# # #     # queue a pop 1, 2 into queue b
# # #     # queue b last element is stack pop element
# # #     def __init__(self):
# # #         self.sim_queue_a = []
# # #         self.sim_queue_b = []
# # #
# # #     # if needed
# # #     # implement a size variable to access queue size (list length)
# # #     # def get_queue_a_size()
# # #
# # #     # push、top、pop 和 empty
# # #
# # #     def push(self, new_element):
# # #         if len(self.sim_queue_a) == 0 and len(self.sim_queue_b) == 0:
# # #             self.sim_queue_a.append(new_element)
# # #         else:
# # #             # push to stack
# # #             if len(self.sim_queue_a) > 0:
# # #                 self.sim_queue_a.append(new_element)
# # #             else:
# # #                 self.sim_queue_b.append(new_element)
# # #
# # #     def top(self):
# # #         # return top element of stack
# # #         # use list len to simulate return of queue size
# # #         result = None
# # #         if len(self.sim_queue_a) > 0:
# # #             while len(self.sim_queue_a) > 0:
# # #                 temp = self.sim_queue_a.pop(0)
# # #                 self.sim_queue_b.append(temp)
# # #                 if len(self.sim_queue_a) == 0:
# # #                     result = temp
# # #         else:
# # #             while len(self.sim_queue_b) > 0:
# # #                 temp = self.sim_queue_b.pop(0)
# # #                 self.sim_queue_a.append(temp)
# # #                 if len(self.sim_queue_b) == 0:
# # #                     result = temp
# # #
# # #         return result
# # #
# # #     def pop(self):
# # #         # return top element of stack
# # #         # use list len to simulate return of queue size
# # #         if len(self.sim_queue_a) > 0:
# # #             while len(self.sim_queue_a) > 0:
# # #                 temp = self.sim_queue_a.pop(0)
# # #                 if len(self.sim_queue_a) == 0:
# # #                     return temp
# # #                 self.sim_queue_b.append(temp)
# # #         else:
# # #             while len(self.sim_queue_b) > 0:
# # #                 temp = self.sim_queue_b.pop(0)
# # #                 if len(self.sim_queue_b) == 0:
# # #                     return temp
# # #                 self.sim_queue_a.append(temp)
# # #
# # #     def empty(self):
# # #         if len(self.sim_queue_a) == 0 and len(self.sim_queue_b) == 0:
# # #             return True
# # #         else:
# # #             return False
# # #
# # #
# # # if __name__ == '__main__':
# # #     # 例如输入数组1、2、4、7、11、15和数字15。由于4+11=15，因此输出4和11。
# # #     # print(Solution().get_sum_of_number([1, 2, 4, 7, 11, 15], 15))
# # #
# # #     # 输入：
# # #     # ["MyStack", "push", "push", "top", "pop", "empty"]
# # #     # [[], [1], [2], [], [], []]
# # #     # 输出：
# # #     # [null, null, null, 2, 2, false]
# # #
# # #     stack = Solution()
# # #     print(stack.push(1))
# # #     print(stack.push(2))
# # #     print(stack.top())
# # #     print(stack.top())
# # #     print(stack.empty())
# # #
# # #
# # #
# #
# # # Understand Basic Data Structure of Python
# # # Heap
# # import heapq
# # import queue
# # class Solution(object):
# #     def heap_review(self, unsorted_array):
# #         heap_list = []
# #         for v in unsorted_array:
# #             heapq.heappush(heap_list, v)
# #         for _ in range(len(heap_list)):
# #             print(heapq.heappop(heap_list))
# #         print(heap_list)
# #
# #     def queue_review(self, unsorted_array):
# #         self.this_queue = queue.Queue()
# #         for v in unsorted_array:
# #             self.this_queue.put(v)
# #         while not self.this_queue.empty():
# #             print(self.this_queue.get())
# #
# #
# # # sliding window
# #
# # # Binary search
# #
# # class Solution3(object):
# #     def b_search(self, sorted_array, target):
# #         l, r = 0, len(sorted_array)
# #         while l < r:
# #             m = (l + r) // 2
# #             if sorted_array[m] < target:
# #                 l = m + 1
# #             else:
# #                 r = m
# #
# #         if 0 <= l < len(sorted_array):
# #             if sorted_array[l] == target:
# #                 return True
# #         return False
# #
# #
# #
# #
# # # DFS & BFS [tree/graph]
# #
# #
# #
# #
# #
# #
# # # Recursion [backtrack]
# #
# # # hashmap
# #
# #
# # if __name__ == '__main__':
# #     # Solution().heap_review([100, 21, 14, 7, 11, 15])
# #     # Solution().queue_review([100, 21, 14, 7, 11, 15])
# #     print(Solution3().b_search([7, 11, 14, 15, 21, 100], 15))
#
#
#
#
# # @lc code=start
# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Codec:
#
#     # 深度遍历
#     # 不使用静态变量 使用递归
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#
#         def recursive_serializer(node, string):
#             if node is None:
#                 string += "null,"
#             else:
#                 string += str(node.val) + ","
#                 string = recursive_serializer(node.left, string)
#                 string = recursive_serializer(node.right, string)
#             print(string)
#             return string
#
#         return recursive_serializer(root, '')
#
#     # 反序列化，将数组转化成二叉树
#     # 使用了递归实现了序列化，侧同理反序列化也使用递归
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype: TreeNode
#         """
#
#         def recursive_serializer(data):
#             if data[0] == "null":
#                 data.pop(0)
#                 return None
#
#             node = TreeNode(data[0])
#             data.pop(0)
#             node.left = recursive_serializer(data)
#             node.right = recursive_serializer(data)
#             return node
#
#         return recursive_serializer(data.split(','))
#
#
#
# if __name__ == '__main__':
#     Codec().deserialize("1,2,3,null,null,4,5")
import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):

        def recur(node, s_string):
            if node is None:
                s_string += "None,"
            else:
                s_string += node.val + "," + recur(node.left, s_string) + recur(node.right, s_string)
            return s_string

        return recur(root, "")


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        iter_array = iter(data)

        def recur():
            val = next(iter_array)
            if val == "None":
                return None
            node = TreeNode(val)
            node.left = recur()
            node.right = recur()
            return node

        return recur()

class GraphSolution(object):

    def bfs(self, graph, start):
        result = []
        searched = set()
        g_queue = queue.Queue()
        g_queue.put(start)

        while not g_queue.empty():
            node = g_queue.get()
            if node not in searched:
                result.append(node)
                searched.add(node)
                for vector in graph[node]:
                    g_queue.put(vector)

        return result


    def dfs(self, graph, start):
        searched = set()
        result = []
        def recur(v):
            if v not in searched:
                searched.add(v)
                result.append(v)
            for vector in graph[v]:
                if vector not in searched:
                    recur(vector)
        recur(start)
        return result


class SlidingWindowPractice(object):
    def find_longest_sub_string_length(self, string):
        non_repeat_chars = set()
        r, result = -1, 0
        for l in range(len(string)):
            if l > 0:
                # remove previous char
                non_repeat_chars.remove(string[l - 1])
            while r + 1 < len(string) and string[r+1] not in non_repeat_chars:
                non_repeat_chars.add(string[r+1])
                r += 1

            result = max(result, r - l + 1)

        return result




class BinarySearchPractice(object):
    def search_in_rotated_sorted_array(self, nums, target):
        """
        [5,7,9,1,2,3]
        :param nums:
        :param target:
        :return:
        """
        length = len(nums)
        # edge case
        if length == 0: return -1
        if target == nums[-1]: return length -1
        if target == nums[0]: return 0
        if nums[0] > nums[-1] and nums[-1] < target < nums[0]: return -1

        l, r = 0, length - 1
        while l < r:
            m = (l + r) // 2

            # edge case
            if target == nums[m]:
                return m
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            elif l == r:
                return -1

            # condition 1 not rotated
            if nums[0] < nums[-1]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # rotated [4,5,6,1,2,3]
                # condition:
                #
                # m in left
                #    - target less than m & less than index 0 - target in right
                #    - target less than m & greater than index 0
                #    - target greater than m
                # m in right
                #
                # m in rotation point
                #    - target in L
                #    - target in R
                if nums[m] > nums[0]: # left
                    if target < nums[0] and target < nums[m]: # 0 - m
                        l = m + 1
                    elif nums[m] > target > nums[0]:
                        r = m - 1
                    elif target > nums[m]:
                        l = m + 1
                    else:
                        return -1
                elif nums[m] < nums[0]: # right
                    # r - m - (-1)
                    if target < nums[m]:
                        r = m - 1
                    elif nums[m] < target < nums[-1]:
                        l = m + 1
                    elif target > nums[-1] and target > nums[m]:
                        r = m - 1
                    else:
                        return -1


        return -1


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        输入：nums = [1,2,1,2,3], k = 2
        输出：7
        解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
        :param nums:
        :param k:
        :return:
        """

        def handler(array, k):
            """
            get most to k sub array from array
            :param array:
            :param k:
            :return:
            """
            l, result = 0, 0
            counter_map = {}
            current_size = 0
            for r in range(len(array)):
                # move r
                # update map and size
                if counter_map.get(array[r], 0) == 0:
                    current_size += 1
                # update occurrence
                counter_map[array[r]] = counter_map.get(array[r], 0) + 1
                while current_size > k:
                    # move l
                    # update l
                    counter_map[array[l]] -= 1
                    if counter_map.get(array[l]) == 0:
                        current_size -= 1
                    l += 1
                # all subarray from l to r = r - l + 1
                result += (r - l) + 1
            return result

        if k == 1:
            return handler(nums, k)
        else:
            return handler(nums, k) - handler(nums, k - 1)


class Solution:
    def encode(self, mat, m, n):
        x = 0
        for i in range(m):
            for j in range(n):
                x = x * 2 + mat[i][j]
        return x

    def decode(self, x, m, n):
        mat = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mat[i][j] = x & 1
                x >>= 1
        return mat

    def convert(self, mat, m, n, i, j):
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            i0, j0 = i + di, j + dj
            if 0 <= i0 < m and 0 <= j0 < n:
                mat[i0][j0] ^= 1

    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        x_start, step = self.encode(mat, m, n), 0
        if x_start == 0:
            return step

        visited = {x_start}
        q = queue.Queue()
        q.put_nowait(x_start)

        while not q.empty():
            step += 1
            k = q.qsize()
            for _ in range(k):
                status = self.decode(q.get_nowait(), m, n)
                for i in range(m):
                    for j in range(n):
                        self.convert(status, m, n, i, j)
                        x_cur = self.encode(status, m, n)
                        if x_cur == 0:
                            return step
                        if x_cur not in visited:
                            visited.add(x_cur)
                            q.put_nowait(x_cur)
                        self.convert(status, m, n, i, j)

        return -1


# import queue
# class Solution:
#     def encode(self, mat, m, n):
#         x = 0
#         for i in range(m):
#             for j in range(n):
#                 x = x * 2 + mat[i][j]
#         return x
#
#     def decode(self, x, m, n):
#         mat = [[0] * n for _ in range(m)]
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 mat[i][j] = x & 1
#                 x >>= 1
#         return mat
#
#     def convert(self, mat, m, n, i, j):
#         for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
#             i0, j0 = i + di, j + dj
#             if 0 <= i0 < m and 0 <= j0 < n:
#                 mat[i0][j0] ^= 1
#
#     def minFlips(self, mat: list[list[int]]) -> int:
#         m, n = len(mat), len(mat[0])
#         x_start, step = self.encode(mat, m, n), 0
#         if x_start == 0:
#             return step
#
#         visited = {x_start}
#         q = queue.Queue()
#         q.put_nowait(x_start)
#
#         while not q.empty():
#             step += 1
#             k = q.qsize()
#             for _ in range(k):
#                 status = self.decode(q.get_nowait(), m, n)
#                 for i in range(m):
#                     for j in range(n):
#                         self.convert(status, m, n, i, j)
#                         x_cur = self.encode(status, m, n)
#                         if x_cur == 0:
#                             return step
#                         if x_cur not in visited:
#                             visited.add(x_cur)
#                             q.put_nowait(x_cur)
#                         self.convert(status, m, n, i, j)
#
#         return -1

if __name__ == '__main__':

    print(BinarySearchPractice().search_in_rotated_sorted_array([5,7,9,1,2,3], 4))


    #         1
    #     2       3
    # null null 4  5
    # data = "1,2,None,None,3,4,None,None,5,None,None,"
    # root = Codec().deserialize(data.split(","))
    # print(root)
    # print(Codec().serialize(root) == data)

    # GRAPH = {
    #     'A': ['B', 'F'],
    #     'B': ['C', 'I', 'G'],
    #     'C': ['B', 'I', 'D'],
    #     'D': ['C', 'I', 'G', 'H', 'E'],
    #     'E': ['D', 'H', 'F'],
    #     'F': ['A', 'G', 'E'],
    #     'G': ['B', 'F', 'H', 'D'],
    #     'H': ['G', 'D', 'E'],
    #     'I': ['B', 'C', 'D'],
    # }
    #
    # print(GraphSolution().bfs(GRAPH, "A"))
    # print(GraphSolution().dfs(GRAPH, "A"))
    #
    #
    # # again
    # print(SlidingWindowPractice().find_longest_sub_string_length([1,2,2,3,4]))



