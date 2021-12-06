#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.56%)
# Likes:    1661
# Dislikes: 209
# Total Accepted:    305.2K
# Total Submissions: 716.5K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Follow up: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    # 34 ms 48% 14.4MB 6%
    """
    因为 寻找 num 的 平方根的值范围是 [1, num]
    如何快速缩小平方根的范围是关键，这里可以采用二分查找实现
    """
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = self.binarySearch(num)
        return sqrt**2 == num

    def binarySearch(self, tgt):
        lo, hi = 1, tgt+1
        while lo < hi:
            mid = (hi-lo)//2 + lo
            mid_val = mid ** 2
            if mid_val > tgt:
                hi = mid
            elif mid_val < tgt:
                lo = mid+1
            elif mid_val == tgt:
                return mid
        return lo
# @lc code=end
so = Solution()

print(so.binarySearch(17))
