#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (52.95%)
# Likes:    3213
# Dislikes: 579
# Total Accepted:    628.1K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times as it
# shows in both arrays and you may return the result in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
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
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 66ms 38% 14.3MB 70%
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
        return i+1
        # n = nums[i]
        # p = i+1
        # while p < len(nums) and nums[p] == n:
        #     p += 1
        # return p
# @lc code=end
so = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]

print(so.intersect(nums1, nums2))