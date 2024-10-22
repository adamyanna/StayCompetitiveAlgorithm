#!/usr/bin/env python3

## Number of Islands https://leetcode.com/problems/number-of-islands/description/
"""
* 岛屿数量 + 战舰甲板
* 1是岛屿，上下左右都是0，就可以作为岛屿（边界也算0）
* 无向图中找到连通分量的总数
* 图的BFS广度优先，需要使用一个 queue、标记结果的hash、结果set
* 用双层嵌套的 for range 循环，找到第一个不为0的i，j坐标
* 通过 queue 记录每次找到的1的坐标，并且将值改为0（放置重复）
* 通过 while 循环访问 queue 中元素的相邻元素，并在循环开始前 pop
* 考虑i，j坐标各自的两种边界条件
* 通过坐标的顺时针移动，左上右下，找到其他为1的点，并加入queue中
* while 循环结束后，给结果+1
"""


# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 分析
        # 1. 从图的左上角开始遍历，找到第一个不是0的点，做为起始点
        # 2. 从起始点开始，使用广度优先 BFS 搜索方法，按照左、上、右、下的方向，搜索为1的点，并将该点保存到push进queue尾部，并将该点设置为0
        # 结果定义
        result = 0
        # 遍历图
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 获取第一个 = 1 的i，j
                # 找到起始点就已经是岛屿的开始了，在找到起始点条件的block之内必然结果+1
                if grid[i][j] == "1":
                    # 起始点，开始BFS
                    # start BFS
                    # 初始化一个 queue，保存i，j
                    queue = [(i, j)]
                    # order > left - up - right - down
                    while queue:
                        # 将 queue 中尾巴元素pop出队列，并将该点值配置为0
                        v_i, v_j = queue.pop(0)
                        grid[v_i][v_j] = "0"
                        # 四种情况
                        # 1. j 大于边界值0
                        # 2. i 大于边界值0
                        # 3. j 小于边界值 len
                        # 4. i 小于边界值 len
                        # 顺时针：L，U，R，D 顺序
                        if v_i > 0:
                            # 如果L值为1，那就符合 ILAND 条件
                            if grid[v_i - 1][v_j] == "1":
                                # 将当前L值的 index 加入 Queue 中，为了避免重复遍历，将结果设置为0值
                                queue.append((v_i - 1, v_j));
                                grid[v_i - 1][v_j] = "0"
                        if v_j > 0:
                            if grid[v_i][v_j - 1] == "1":
                                queue.append((v_i, v_j - 1));
                                grid[v_i][v_j - 1] = "0"
                        if v_i < len(grid) - 1:
                            if grid[v_i + 1][v_j] == "1":
                                queue.append((v_i + 1, v_j));
                                grid[v_i + 1][v_j] = "0"
                        if v_j < len(grid[0]) - 1:
                            if grid[v_i][v_j + 1] == "1":
                                queue.append((v_i, v_j + 1));
                                grid[v_i][v_j + 1] = "0"
                                # 直到跳出 while 循环，表示当前 queue 为空，切queue中queue尾部元素的L、U、R、D值都为0，认为成功找到了一个岛屿

                    # 岛屿数量+1
                    result += 1

        return result