#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (61.77%)
# Likes:    8071
# Dislikes: 583
# Total Accepted:    820.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
# 
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        abcde :
        pos   left    right
        a       _       bcde
        b       a       cde
        c       ab      de
        d       abc     e
        e       abcd    _
        根据规律计算 left and right，最后 * 即可
        注意删除循环运算中的最后一位 abcde
        """
        pre, post = [1], [1]
        for num in nums:
            tmp = pre[-1] * num
            pre.append(tmp)
        for num in reversed(nums):
            tmp = post[-1] * num
            post.append(tmp)
        pre = pre[ :-1]
        post = post[ :-1]
        post.reverse()

        r = []
        for pr, po in zip(pre, post):
            r.append(pr * po)
        return r
# @lc code=end

if __name__=='__main__':
    so = Solution()
    nums = [1,2,3,4]
    nums = [-1,1,0,-3,3]
    r = so.productExceptSelf(nums)
    print(r)
