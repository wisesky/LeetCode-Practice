#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (58.95%)
# Likes:    6173
# Dislikes: 180
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        pos = -1
        length = len(nums)
        for i in range(length):
            if nums[i] == 0 :
                if pos == -1:
                    pos = i
            elif pos!=-1:
                self.exch(pos, i)
                pos += 1

    def exch(self, i, j):
        tmp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = tmp

# @lc code=end

so = Solution()
nums = [1,0,0]
so.moveZeroes(nums)
print(nums)