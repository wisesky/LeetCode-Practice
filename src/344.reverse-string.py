#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (72.02%)
# Likes:    3181
# Dislikes: 840
# Total Accepted:    1.2M
# Total Submissions: 1.7M
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters s.
# 
# 
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
# 
# 
# 
# Follow up: Do not allocate extra space for another array. You must do this by
# modifying the input array in-place with O(1) extra memory.
# 
#
from typing import List
# @lc code=start
class Solution:
    # 236ms(36%) 18.5MB(61%)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lo, hi = 0, len(s)-1

        while lo < hi :
            tmp = s[lo]
            s[lo] = s[hi]
            s[hi] = tmp

            lo += 1
            hi -= 1
        return
# @lc code=end

so = Solution()

s = list('abc0123')
so.reverseString(s)
print(s)