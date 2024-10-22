#!/usr/bin/env python3

# course-schedule
# <Same as course-schedule-ii>


##############################
# Review of Graph
# connected (just V connect to V) / directed (V point to V)
# Vertices (node) / Edges (lines)
# Directed Graph
#       - OutDegree (how much pointer point out from V)
#       - InDegree (how much pointer point V)

##############################


##############################
# course-schedule-ii
# 1. Save edges from prerequisites, key is V & value is Edge, map[v[1]] = v[0], from v[1] -> v[0](point to)
# 2. Save all InDegree to all V with a Array (Array can access V with 0 InDegree)
# 3. Init a Queue, Append all 0 InDegree to Queue (BFS: start with 0 InDegree V)
# 4. BFS to Queue, and InDegree-1 for every Edge[V] (V pointer others) append to result
##############################

import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        # 将所有入度为 0 的节点放入队列中
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            # 从队首取出一个节点
            u = q.popleft()
            # 放入答案中
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if indeg[v] == 0:
                    q.append(v)

        if len(result) != numCourses:
            result = list()
        return result
