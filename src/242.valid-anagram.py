#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (59.41%)
# Likes:    2920
# Dislikes: 171
# Total Accepted:    874.9K
# Total Submissions: 1.5M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length = len(s)
        d1 = {}
        d2 = {}
        for i in range(length):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1
            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1
        for key in d1:
            if d2.get(key) != d1[key]:
                return False
        return True
# @lc code=end
so = Solution()
s = "anagram"
t = "nagaram"
s='cat'
t='rat'
r = so.isAnagram(s, t)
print(r)