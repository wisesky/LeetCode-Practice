#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (55.18%)
# Likes:    846
# Dislikes: 1964
# Total Accepted:    253K
# Total Submissions: 458.1K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend:
# 
# 
# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the
# heap.
# The one who removes the last stone is the winner.
# 
# 
# Given n, the number of stones in the heap, return true if you can win the
# game assuming both you and your friend play optimally, otherwise return
# false.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: false
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last
# stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last
# stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: n = 2
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    """
    DFS error: maximum recursion depth exceeded
    """
    # def __init__(self) -> None:
    #     self.win = set([1,2,3])
    # def canWinNim(self, n: int) -> bool:
    #     if n in self.win:
    #         return True
        
    #     win_1 = not self.canWinNim(n-1)
    #     win_2 = not self.canWinNim(n-2)
    #     win_3 = not self.canWinNim(n-3)
    #     win = win_1 or win_2 or win_3
    #     if win:
    #         self.win.add(n)
    #     return win

    def canWinNim(self, n):
        """
        每隔3就存在一个必败节点
        123, 4, 567, 8,
        """
        return n % 4 != 0
# @lc code=end

so = Solution()
print(so.canWinNim(1348820612))
print(so.canWinNim(4))