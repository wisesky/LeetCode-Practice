#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (59.92%)
# Likes:    3004
# Dislikes: 360
# Total Accepted:    254.5K
# Total Submissions: 422.2K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# The board is made up of an m x n grid of cells, where each cell has an
# initial state: live (represented by a 1) or dead (represented by a 0). Each
# cell interacts with its eight neighbors (horizontal, vertical, diagonal)
# using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# The next state is created by applying the above rules simultaneously to every
# cell in the current state, where births and deaths occur simultaneously.
# Given the current state of the m x n grid board, return the next state.
# 
# 
# Example 1:
# 
# 
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# 
# 
# Example 2:
# 
# 
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
# 
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated
# simultaneously: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# upon the border of the array (i.e., live cells reach the border). How would
# you address these problems?
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        height = len(board)
        if height == 0:
            return
        width = len(board[0])
        self.height = height
        self.width = width
        
        die2Live = []
        live2Die = []
        for i in range(height):
            for j in range(width):
                if board[i][j] == 0 and self.isDie2Live(i,j):
                    # board[i][j] = 1
                    die2Live.append((i,j))
                if board[i][j] == 1 and self.isLive2Die(i, j):
                    # board[i][j] = 0
                    live2Die.append((i,j))
        
        for i,j in die2Live:
            board[i][j] = 1
        for i,j in live2Die:
            board[i][j] = 0
        return

    def isDie2Live(self,i,j):
        die, live = self.checkNeigh(i, j)
        return live == 3

    def isLive2Die(self, i, j):
        die, live = self.checkNeigh(i, j)
        return live < 2 or live > 3

    def checkNeigh(self, i,j):
        """
        return 0_num, 1_num
        """
        die, live = 0, 0
        for x in [i-1,i,i+1]:
            for y in [j-1,j,j+1]:
                if x==i and y==j:
                    continue
                if x >=0 and x<self.height \
                    and y>=0 and y<self.width:
                        if self.board[x][y]==0:
                            die += 1
                        elif self.board[x][y]==1:
                            live += 1
        return die, live

# @lc code=end

board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]

so = Solution()
so.gameOfLife(board)
print(so.checkNeigh(1,0))