#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (39.24%)
# Likes:    1484
# Dislikes: 1473
# Total Accepted:    350K
# Total Submissions: 887.9K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        marked = {}
        for pos, num in enumerate(nums):
            if num not in marked:
                marked[num] = pos
            else:
                itv = pos - marked[num]
                if itv <= k:
                    return True
                else:
                    marked[num] = pos
        else:
            return False
# @lc code=end
if __name__ == "__main__":
    so = Solution()
    nums = [1,0,1,1]
    k = 1
    nums = [1,2,3,1,2,3]
    k = 2
    r = so.containsNearbyDuplicate(nums, k)
    print(r)
