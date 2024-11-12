#!/usr/bin/env python3

"""
course-schedule

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation:
    There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
    So it is impossible.
"""

import queue
class Solution1(object):
    def course_schedule(self, numCourses, prerequisites):
        """
        [[1,0],[0,1]]
        - Graph
        - 1 <- 0
        - save in_degree for each node
            in_degree[1] = 1
        - save edge for each vertex at index 1
            edge_map[1] = [0]
        :return:
        """

        edge_map = {}
        in_degree = [0] * numCourses

        result = []

        for v in prerequisites:
            if v[1] not in edge_map:
                edge_map[v[1]] = []
            edge_map[v[1]].append(v[0])
            in_degree[v[0]] += 1

        q = queue.Queue()
        for vertex, in_d in enumerate(in_degree):
            if in_d == 0:
                q.put(vertex)

        if q.empty(): return False

        while not q.empty():
            vertex = q.get()
            result.append(vertex)
            if vertex not in edge_map:
                continue
            for v in edge_map[vertex]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.put(v)

        if len(result) != numCourses:
            return False

        return True


"""
course-schedule ii

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3], [0,2,1,3]
Explanation: 
    There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. 
    Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
"""

"""
Graph
edge
  * connected
    - v connect to v
  * directed
    - v point to v
    - out_degree
        - how much point out from v
    - in_degree
        - how much point in to v
"""

import queue
class Solution2(object):
    def course_schedule(self, num, course_list):
        # save graph
        edges = dict()
        # save in_degree
        in_degree = [0] * num

        result = list()

        # [[1,0],[2,0],[3,1],[3,2]]
        # 1, 2 before 3
        # 3 <- 1
        # 3 <- 2
        # save - in_degree number of each vertex {in_degree[3] = 2}
        # save - edge of each vertex {edge_map[0] = [1,2]}

        for v in course_list:
            if v[1] not in edges:
                edges[v[1]] = []
            edges[v[1]].append(v[0])
            in_degree[v[0]] += 1

        q = queue.Queue()
        for v, n in enumerate(in_degree):
            # take the course which is in degree is 0
            if n == 0:
                q.put(v)

        while not q.empty():
            c = q.get()
            result.append(c)
            # get all vertice which c point at
            if c not in edges:
                continue
            for vertex in edges[c]:
                in_degree[vertex] -= 1
                if in_degree[vertex] == 0:
                    # class to take
                    q.put(vertex)

        if len(result) != num:
            return []
        return result


if __name__ == '__main__':
    print(Solution1().course_schedule(3, [[1,0],[2,0],[0,1]]))
    print(Solution1().course_schedule(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(Solution2().course_schedule(4, [[1,0],[2,0],[3,1],[3,2]]))










