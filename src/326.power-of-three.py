#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (42.54%)
# Likes:    398
# Dislikes: 50
# Total Accepted:    383.1K
# Total Submissions: 897.3K
# Testcase Example:  '27'
#
# Given an integer n, return true if it is a power of three. Otherwise, return
# false.
# 
# An integer n is a power of three, if there exists an integer x such that n ==
# 3^x.
# 
# 
# Example 1:
# Input: n = 27
# Output: true
# Example 2:
# Input: n = 0
# Output: false
# Example 3:
# Input: n = 9
# Output: true
# Example 4:
# Input: n = 45
# Output: false
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

# @lc code=start
class Solution:
    """
    60ms(97%) 14.2MB(76%)
    DFS: 注意边界情况 n==1 应该在 n%3!=0 前
    因为 1%3!=0 却是True
    """
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 3 != 0 or n == 0:
            return False
    
        return self.isPowerOfThree(n//3)
        
# @lc code=end
so = Solution()
print(so.isPowerOfThree(27))