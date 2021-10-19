#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (39.80%)
# Likes:    1438
# Dislikes: 149
# Total Accepted:    174.2K
# Total Submissions: 437.6K
# Testcase Example:  '5\n7'
#
# Given two integers left and right that represent the range [left, right],
# return the bitwise AND of all numbers in this range, inclusive.
# 
# 
# Example 1:
# 
# 
# Input: left = 5, right = 7
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: left = 0, right = 0
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: left = 1, right = 2147483647
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= left <= right <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bin_left = bin(left)[2: ]
        bin_right = bin(right)[2: ]
        if len(bin_left) != len(bin_right):
            return 0
        pos = 0
        for le, ri in zip(bin_left, bin_right):
            if le != ri:
                break
            pos += 1
        r = bin_left[ :pos] + '0'*(len(bin_left)-pos)
        return int(r,2)

# if __name__ == "__main__":
#     left = 1
#     right = 2147483647
#     so = Solution()
#     r = so.rangeBitwiseAnd(left, right)
#     print(r)
# @lc code=end

