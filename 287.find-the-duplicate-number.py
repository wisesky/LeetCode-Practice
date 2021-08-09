#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (58.13%)
# Likes:    8671
# Dislikes: 906
# Total Accepted:    580.4K
# Total Submissions: 998.3K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
# 
# There is only one repeated number in nums, return this repeated number.
# 
# You must solve the problem without modifying the array nums and uses only
# constant extra space.
# 
# 
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# Input: nums = [1,1]
# Output: 1
# Example 4:
# Input: nums = [1,1,2]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
# 
# 
# 
# Follow up:
# 
# 
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = len(nums) - 1
        # s = n * (n+1) // 2
        # return sum(nums) - s
        nums.sort()
        length = len(nums)
        for i in range(1, length):
            if nums[i] == nums[i-1]:
                return nums[i]
# @lc code=end

