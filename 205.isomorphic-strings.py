#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (40.85%)
# Likes:    2155
# Dislikes: 488
# Total Accepted:    372.1K
# Total Submissions: 910.4K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
# 
# 
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
# 
# 
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        singleT = set()
        for x,y in zip(s, t):
            if x in s2t and s2t[x] != y:
                return False
            elif x not in s2t:
                if y in singleT:
                    return False
                s2t[x] = y
                singleT.add(y)
            else: # s2t[x] == y
                pass
            
        return True

# @lc code=end

