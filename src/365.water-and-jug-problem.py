#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#
# https://leetcode.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (32.66%)
# Likes:    604
# Dislikes: 987
# Total Accepted:    54.5K
# Total Submissions: 165.5K
# Testcase Example:  '3\n5\n4'
#
# You are given two jugs with capacities jug1Capacity and jug2Capacity liters.
# There is an infinite amount of water supply available. Determine whether it
# is possible to measure exactly targetCapacity liters using these two jugs.
# 
# If targetCapacity liters of water are measurable, you must have
# targetCapacity liters of water contained within one or both buckets by the
# end.
# 
# Operations allowed:
# 
# 
# Fill any of the jugs with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full,
# or the first jug itself is empty.
# 
# 
# 
# Example 1:
# 
# 
# Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
# Output: true
# Explanation: The famous Die Hard example 
# 
# 
# Example 2:
# 
# 
# Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        tgts = set()
        c1 , c2 = (jug1Capacity, jug2Capacity) if jug1Capacity < jug2Capacity \
            else (jug2Capacity, jug1Capacity)
        
        val = abs(c2-c1)
        i = 0
        while val not in tgts:
            if val == targetCapacity:
                return True
            tgts.update([val])
            c = c1 if i%2==0 else c2
            i += 1
            val = abs(c - val)

        return False

        # have = self.comb(jug1Capacity, jug2Capacity)

        # need = {}
        # if 0 in have:
        #     have.remove(0)
        # for num in have:
        #     if num in need:
        #         return True
        #     need[targetCapacity-num] = num
        # return False

    # def comb(self,s1, s2):
    #     """
    #      返回所有s1 s2 的组合
    #     """
    #     if s1 > s2:
    #         s1, s2 = s2, s1

    #     r = set()
    #     s = s1
    #     while s1 < s2:
    #         r.update([s1])
    #         r.update([s2-s1])
    #         s1 += s
    #     r.update([s2])
    #     r.update([s1-s2])
    #     return r
        
    def contain(self, s1 ,s2):
        """
        s1 in s2
        params:
        s1 : set
        s2 : set
        """
        return s1.issubset(s2)
        # itc = set(s1) & set(s2)
        # return len(itc) > 0
# @lc code=end
so = Solution()

# print(so.comb(13,11))
j1 = 1
j2 = 2
t = 3

print(so.canMeasureWater(j1, j2, t))
