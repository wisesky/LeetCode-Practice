#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (47.18%)
# Likes:    3927
# Dislikes: 68
# Total Accepted:    254.5K
# Total Submissions: 534.2K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
# 
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        564ms(37%) 16MB(52%) 包含环检测 inStack
        741ms(13%) 16MB(54%) 不包含环检测 inStack

        可以将 matrix 抽象成图，合法的递增邻接元素，构成了边
        首先可以确定的是，这是一个 DAG， 因为递增序列的性质保证了不可能出现环
        如果有 a->b 的边， 那么 a_longest_path = b_longest_path + 1
        符合 Dijkstra 算法的最优子结构，所以可以用 DFS 遍历所有节点，同时memo中间的遍历节点

        实践发现，如果包含环检测的DFS(inStack) 会快一点，可能是因为比合法的longest_path检测要更快一点
        此外，符合这个递推式的结构，应该可以改写成迭代和DP，不过因为这是树结构，DFS显然更加方便，改写成迭代或许会处理很多边界情况
        """
        distTo = {}
        inStack = set()
        height = len(matrix)
        width = len(matrix[0])
        res = 0

        for i in range(height):
            for j in range(width):
                r = self.dfs(i,j, matrix, distTo, inStack)
                res = max(r, res)
        return res

    def dfs(self, i, j ,matrix, distTo, inStack):
        """
        i,j -> start ==> longest increasing path
        """
        if (i,j) in distTo:
            return distTo[i, j]

        # inStack.add( (i,j) )
        adjs = [
            [i-1,j],
            [i+1,j],
            [i,j-1],
            [i,j+1]
        ]
        r = 0
        for x,y in adjs:
            if x >= 0  and x < len(matrix) \
                and y >=0 and y < len(matrix[0]) :
                # if (x,y) in inStack:
                    # continue
                if matrix[x][y] > matrix[i][j]:
                    r = max(r, self.dfs(x,y,matrix,distTo, inStack))
        
        # inStack.remove( (i,j) )
        distTo[i,j] = r + 1
        return r + 1

# @lc code=end

so = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
# matrix = [[3,4,5],[3,2,6],[2,2,1]]
# matrix = [[1]]
print(so.longestIncreasingPath(matrix))