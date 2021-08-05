#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (46.00%)
# Likes:    5199
# Dislikes: 96
# Total Accepted:    474.2K
# Total Submissions: 1M
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
#   '5'
#
# Write an efficient algorithm that searches for a target value in an m x n
# integer matrix. The matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
# 
# 
#
from typing import List
# @lc code=start
class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    heigth = len(matrix)
    if heigth == 0:
      return 0
    width = len(matrix[0])

    first = []
    for i in range(heigth):
      first.append(matrix[i][0])
    x_pos = self.binSearch(first, target)
    
    if x_pos<heigth and  matrix[x_pos][0] == target:
      return True
    
    for i in range(x_pos):
      y_pos = self.binSearch(matrix[i], target)
      if y_pos >= width:
        continue
      if matrix[i][y_pos] == target:
        return True
    return False

  def binSearch(self, li, target):
    lo, hi = 0, len(li)-1
    while lo <= hi:
      mid = (lo+hi) // 2
      if li[mid] == target:
        return mid
      elif li[mid] < target:
        lo = mid+1
      else: # li[mid] > target
        hi = mid-1
    return lo

# @lc code=end

if __name__=='__main__':
  so = Solution()
  # matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
  # target = 20
  matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
  target = 19
  matrix = [[1,1]]
  target=2
  matrix = [[-1],[-1]]
  target = -2
  # matrix = [[-1,3]]
  # target = 3
  # matrix=[[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]
  # target = 13
  r = so.searchMatrix(matrix, target)
  print(r)