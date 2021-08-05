#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (51.65%)
# Likes:    3325
# Dislikes: 536
# Total Accepted:    642.4K
# Total Submissions: 1.2M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
# 
# A happy number is a number defined by the following process:
# 
# 
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# 
# 
# Return true if n is a happy number, and false if not.
# 
# 
# Example 1:
# 
# 
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: false
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
    def isHappy(self, n: int) -> bool:
        marked = set()
        return self.helper(n, marked)

    def helper(self, n, marked):
        str_n = str(n)
        # if len(str_n) < 2:
        #     return False
        if str_n in marked:
            return False
        
        ss = 0
        for s in str_n:
            ss += int(s)**2
        if ss == 1 :
            return True

        marked.add(str_n)
        return self.helper(ss, marked)


# @lc code=end

