#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (30.96%)
# Likes:    1756
# Dislikes: 156
# Total Accepted:    118.6K
# Total Submissions: 382.7K
# Testcase Example:  '"aacecaaa"'
#
# You are given a string s. You can convert s to a palindrome by adding
# characters in front of it.
# 
# Return the shortest palindrome you can find by performing this
# transformation.
# 
# 
# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of lowercase English letters only.
# 
# 
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        l = []
        l.pop( )
# @lc code=end

