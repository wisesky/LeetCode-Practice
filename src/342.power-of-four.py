#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (42.57%)
# Likes:    1112
# Dislikes: 267
# Total Accepted:    255.9K
# Total Submissions: 598.7K
# Testcase Example:  '16'
#
# Given an integer n, return true if it is a power of four. Otherwise, return
# false.
# 
# An integer n is a power of four, if there exists an integer x such that n ==
# 4^x.
# 
# 
# Example 1:
# Input: n = 16
# Output: true
# Example 2:
# Input: n = 5
# Output: false
# Example 3:
# Input: n = 1
# Output: true
# 
# 
# Constraints:
# 
# 
# -2^31 <= n <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without loops/recursion?
#
import math
# @lc code=start
class Solution:
    # 40 ms(33%) 14.3MB(6%)
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 :
            return False
        x = math.log(n, 4) 
        return int(x) == x
# @lc code=end

so = Solution()

print(so.isPowerOfFour(-64))