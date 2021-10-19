#
# @lc app=leetcode id=335 lang=python3
#
# [335] Self Crossing
#
# https://leetcode.com/problems/self-crossing/description/
#
# algorithms
# Hard (28.96%)
# Likes:    205
# Dislikes: 427
# Total Accepted:    26.3K
# Total Submissions: 90.8K
# Testcase Example:  '[2,1,1,2]'
#
# You are given an array of integers distance.
# 
# You start at point (0,0) on an X-Y plane and you move distance[0] meters to
# the north, then distance[1] meters to the west, distance[2] meters to the
# south, distance[3] meters to the east, and so on. In other words, after each
# move, your direction changes counter-clockwise.
# 
# Return true if your path crosses itself, and false if it does not.
# 
# 
# Example 1:
# 
# 
# Input: distance = [2,1,1,2]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: distance = [1,2,3,4]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: distance = [1,1,1,1]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= distance.length <= 10^5
# 1 <= distance[i] <= 10^5
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        num0 = sum(distance[ : :4])
        num1 = sum(distance[1: :4])
        num2 = sum(distance[2: :4])
        num3 = sum(distance[3: :4])
        si = -1
        i = 0
        while i < len(distance) and distance[i] > si:
            si = distance[i]
            i += 2
        
        j = 1
        sj = -1
        while j<len(distance) and distance[j] > sj:
            sj = distance[j]
            j += 2

        # return distance[2] <= distance[0] and distance[3] >= distance[1]
        # return num2<=num0 and num3>=num1
        if num2<=num0 and num3>=num1:
            if i >= len(distance) and j >= len(distance):
                return False
            else:
                return True
# @lc code=end
so = Solution()

nums = [1,1,2,1,1]
# nums = [1,2,2,3,4]
nums = [1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1]
print(so.isSelfCrossing(nums))