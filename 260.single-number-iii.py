#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (65.59%)
# Likes:    2575
# Dislikes: 143
# Total Accepted:    200.8K
# Total Submissions: 305.7K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an integer array nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once. You can return the answer in any order.
# 
# You must write an algorithm that runs in linear runtime complexity and uses
# only constant extra space.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0]
# Output: [-1,0]
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,1]
# Output: [1,0]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each integer in nums will appear twice, only two integers will appear once.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.append(float('inf'))
        nums.append(float('inf'))
        r = []
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                r.append(nums[i-1])
                i += 1
                if len(r) == 2:
                    break
            else:
                i += 2
        return r

# @lc code=end

so = Solution()
# nums = [-1,0]
nums = [1,2,1,3,2,5]
print(so.singleNumber(nums))