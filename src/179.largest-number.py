#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (31.18%)
# Likes:    3190
# Dislikes: 326
# Total Accepted:    254.5K
# Total Submissions: 816.1K
# Testcase Example:  '[10,2]'
#
# Given a list of non-negative integers nums, arrange them such that they form
# the largest number.
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,2]
# Output: "210"
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Example 3:
# 
# 
# Input: nums = [1]
# Output: "1"
# 
# 
# Example 4:
# 
# 
# Input: nums = [10]
# Output: "10"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
# 
# 
#
from typing import List
from functools import cmp_to_key
# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=cmp_to_key(cmp) ,reverse=True)
        return str(int(''.join([str(x) for x in nums])))

# def cmp(x, y):
#     if x == y:
#         return 0
    
#     str_x, str_y = str(x), str(y)
#     length = min(len(str_x), len(str_y))
#     if str_x[ :length] == str_y[ :length]:
#         if len(str_x)>length:
#             return 1 if str_x[length] > str_x[0] else -1
#         if len(str_y)>length:
#             return -1 if str_y[length] > str_y[0] else 1
#     for i,j in zip(str_x[ :length], str_y[ :length]):
#         if i != j:
#             return 1 if i > j else -1

def cmp(x, y):
    if x == y:
        return 0
    str_x , str_y = str(x), str(y)
    s1 = ''.join([str_x, str_y])
    s2 = ''.join([str_y, str_x])
    return 1 if s1 > s2 else -1

if __name__=='__main__':
    so = Solution()
    # nums = [34323,3432]
    nums = [3,30,34,5,9]
    r = so.largestNumber(nums)
    print(r)
# @lc code=end

