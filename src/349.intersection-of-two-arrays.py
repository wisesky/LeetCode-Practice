#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (67.01%)
# Likes:    1989
# Dislikes: 1746
# Total Accepted:    556.4K
# Total Submissions: 826.4K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 94ms(8%) 14.5MB(13%)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        r = []
        p1 , p2 = 0,0
        while p1 < len(nums1) and p2 < len(nums2):
            n1 = nums1[p1]
            n2 = nums2[p2]
            if n1 > n2:
                p2 = self.nextPoint(nums2, p2)
            elif n1 < n2:
                p1 = self.nextPoint(nums1, p1)
            elif n1 == n2:
                r.append(n1)
                p1 = self.nextPoint(nums1, p1)
                p2 = self.nextPoint(nums2, p2)

        return r
        
    def nextPoint(self, nums, i):
        n = nums[i]
        p = i+1
        while p < len(nums) and nums[p] == n:
            p += 1
        return p
# @lc code=end
so = Solution()

nums1 = [1,1,2,2]
nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(so.intersection(nums1, nums2))