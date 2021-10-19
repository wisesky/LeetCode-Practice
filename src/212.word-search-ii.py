#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (37.77%)
# Likes:    3927
# Dislikes: 147
# Total Accepted:    314.4K
# Total Submissions: 831.8K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#   '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
# 
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# 
# 
# Example 2:
# 
# 
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# 
# 
#
from typing import List
# @lc code=start
"""
Time: 8.6s (18%)
Memory: 14.6 MB (40%)
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
      height = len(board)
      if height == 0:
        return []
      width = len(board[0])
      # construct char to pos
      char2pos = {}
      for i in range(height):
        for j in range(width):
          char = board[i][j]
          if char in char2pos:
            char2pos[char].append((i,j))
          else:
            char2pos[char] = [(i,j)]
      
      res = []
      marked = {}
      for word in words:
        for pos in char2pos.get(word[0], [None]):
          if pos != None :
            marked[pos[0],pos[1]] = True
            flag = self.findWord(board, marked,char2pos,pos[0],pos[1],word[1: ])
            marked[pos[0],pos[1]] = False
            if flag:
              res.append(word)
              break
      return res

    def findWord(self, board,marked,char2pos, x,y,word):
      if len(word) == 0:
        return True
      height = len(board)
      width = len(board[0])
      candidate1 = [
        (x-1,y), # up
        (x,y-1), # left
        (x,y+1), # right
        (x+1,y) # down
      ]
      candidate2 = char2pos.get(word[0], None)
      marked[x,y] = True
      if candidate2 == None:
        return False
      c1 = set(candidate1)
      c2 = set(candidate2)
      c = c1.intersection(c2)
      for i,j in c:
        if marked.get((i,j), False):
          continue
        # val = board[i][j]
        # if val == word[0]:
        
        flag = self.findWord(board,marked,char2pos, i,j,word[1: ]) 
        if flag:
          marked[x,y] = False
          return True
      marked[x,y] = False
      return False
# @lc code=end
if __name__ == "__main__":
  board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
  words = ["oa","oaa",'oao']
  # board = [["a","a"]]
  # words = ["aaa"]
  # board = [["a","b"]]
  # words = ["ab"]
  so = Solution()
  r = so.findWords(board, words)
  print(r)
