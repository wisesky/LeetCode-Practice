#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (45.32%)
# Likes:    3788
# Dislikes: 178
# Total Accepted:    288.6K
# Total Submissions: 633.4K
# Testcase Example:  '"()())()"'
#
# Given a string s that contains parentheses and letters, remove the minimum
# number of invalid parentheses to make the input string valid.
# 
# Return all the possible results. You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "()())()"
# Output: ["(())()","()()()"]
# 
# 
# Example 2:
# 
# 
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# 
# 
# Example 3:
# 
# 
# Input: s = ")("
# Output: [""]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.
# 
# 
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
# @lc code=end

