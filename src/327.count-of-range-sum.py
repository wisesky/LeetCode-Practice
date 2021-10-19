#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (36.25%)
# Likes:    1246
# Dislikes: 136
# Total Accepted:    53.5K
# Total Submissions: 147.9K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums and two integers lower and upper, return the
# number of range sums that lie in [lower, upper] inclusive.
# 
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j inclusive, where i <= j.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their
# respective sums are: -2, -1, 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0], lower = 0, upper = 0
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# -10^5 <= lower <= upper <= 10^5
# The answer is guaranteed to fit in a 32-bit integer.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        TLE: ans = 80000
        O(n**2)
        """
        rangeSum = []
        r = 0

        for num in nums:
            rangeSum = [x+num for x in rangeSum]
            rangeSum.append(num)
            # for rs in rangeSum:
            #     if rs >= lower and rs <= upper:
            #         r += 1
            tmp = [1 if x>=lower and x<=upper else 0 for x in rangeSum]
            r += sum(tmp)
        return r

    def countRangeSum(self,nums, lower, upper):
    #   """
    #   TLE: ans = 29478761
    #   """
        rangeSum = []
        r = 0

        for num in nums:
            rangeSum = [x+num for x in rangeSum]
            pos = self.biLeftSearch(rangeSum, num)
            rangeSum.insert(pos, num)
            left = self.biLeftSearch(rangeSum, lower)
            right = self.biRigthSearch(rangeSum, upper)
            r += right - left
            
        return r

    def biLeftSearch(self,li, val):
        """
        binary search left boundry
        """
        lo, hi = 0, len(li)
        while lo < hi:
            mid = lo + (hi-lo)//2
            if li[mid] >= val:
                hi = mid
            else:
                lo = mid+1
        return lo

    def biRigthSearch(self, li, val):
        """
        binary search rigth boundry
        """
        lo, hi = 0, len(li)
        while lo < hi:
            mid = lo + (hi-lo)//2
            if li[mid] <= val:
                lo = mid + 1
            else:
                hi = mid
        # return lo - 1
        return lo
# @lc code=end

so = Solution()

nums = [-2,5,-1]
lower = -2
upper = 2

nums = [0]
lower = 0
upper = 0

nums=  [-1,1]
lower = 0
upper = 0

nums = [2147483647,-2147483648,-1,0]
lower = -1
upper = 0
print(so.countRangeSum(nums, lower, upper))