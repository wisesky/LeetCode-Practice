#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (39.68%)
# Likes:    3011
# Dislikes: 229
# Total Accepted:    215.3K
# Total Submissions: 542.5K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,2,3]
# Output: [3]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
#
from typing import List
import math
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        threshold = length // 3
        nums.sort()

        res = []
        count = 1
        for i in range(1, length):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                if count > threshold:
                    res.append(nums[i-1])
                count = 1
        else:
            if count > threshold:
                res.append(nums[length-1])
        return res
# @lc code=end

if __name__=='__main__':
    so = Solution()
    nums = [1,2]
    nums = [3,2,3]
    r = so.majorityElement(nums)
    print(r)
