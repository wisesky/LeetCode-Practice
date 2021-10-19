#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (31.10%)
# Likes:    1654
# Dislikes: 711
# Total Accepted:    105.7K
# Total Submissions: 337.9K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2]
# < nums[3]....
# 
# You may assume the input array always has a valid answer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 5000
# It is guaranteed that there will be an answer for the given input nums.
# 
# 
# 
# Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
#
from typing import List
# @lc code=start
class Solution:
    """
    166ms(64%) 17MB(90%)
    结果是 bottom peak bottom peak 的模式
    排序之后，中间截断，分为 lower upper 两端， 分别从高位到地位轮流加入nums
    注意因为允许重复数字出现，
    如果从低位到高位，可能出现upper 低位 == lower 高位的情况
    eg 4 ,5 , 5, 6 
    低位-到高位: 4,5,5,6
    高位到低位: 5,6,5,4
    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        length = len(nums)
        mid = length // 2 if length%2==0 else length//2 + 1
        
        left = nums[ :mid].copy()
        right = nums[mid: ].copy()
        nums.clear()

        left.reverse()
        right.reverse()
        for i, j in zip(left, right):
            nums.append(i)
            nums.append(j)

        if len(left) > len(right):
            nums.append(left[-1])

        return

# @lc code=end

nums = [1,5,2,3,4,6]
# nums = [1,3,2,2,3,1]
so = Solution()
so.wiggleSort(nums)
print(nums)