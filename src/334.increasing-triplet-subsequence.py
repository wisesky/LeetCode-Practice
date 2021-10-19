#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (41.01%)
# Likes:    2942
# Dislikes: 180
# Total Accepted:    225.1K
# Total Submissions: 548.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
# indices exists, return false.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# 
# 
# Example 3:
# 
# 
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] ==
# 4 < nums[5] == 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you implement a solution that runs in O(n) time complexity
# and O(1) space complexity?
#
from typing import List
# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        921ms(12%) 25.5MB(15%)
        可以利用最长递增子序列的dp算法，计算最长递增子序列的长度，最后返回序列长度
        """
        dp = []
        for num in nums:
            index = self.biSearch(dp, num)
            if index >= len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp) >= 3
        
    def biSearch(self, nums, tgt):
        """
        nums: List
        tgt: int
        return type: int : tgt在nums index
        
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi-lo)//2
            val = nums[mid]
            if val > tgt:
                hi = mid
            elif val < tgt:
                lo = mid + 1
            elif val == tgt:
                return mid

        return lo
# @lc code=end

so = Solution()

nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
nums = [2,1,5,0,4,6]


print(so.increasingTriplet(nums))