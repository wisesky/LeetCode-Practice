#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (50.31%)
# Likes:    8824
# Dislikes: 250
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        height = len(grid)
        if height == 0:
            return count
        width = len(grid[0])
        marked = set()
        for x in range(height):
            for y in range(width):
                if grid[x][y] == '1' and (x,y) not in marked:
                    self.dfs(x,y, grid, marked)
                    count += 1

        return count

    def dfs(self, x, y, grid,marked):
        marked.add((x,y))
        around = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        around = [(nx,ny) for nx,ny in around \
                    if nx>=0 and nx<len(grid) and \
                     ny>=0 and ny<len(grid[0])    ]
        for nx,ny in around:
            if grid[nx][ny] == '1' and (nx,ny) not in marked:
                self.dfs(nx,ny,grid, marked)
        return 1

# if __name__ == "__main__":
#     so = Solution()
#     grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
#     grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#     r = so.numIslands(grid)
#     print(r)
# @lc code=end

