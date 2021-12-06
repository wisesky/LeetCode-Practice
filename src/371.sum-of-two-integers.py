#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (50.71%)
# Likes:    2019
# Dislikes: 3123
# Total Accepted:    253.4K
# Total Submissions: 499.7K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return the sum of the two integers without using
# the operators + and -.
# 
# 
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
# 
# 
# Constraints:
# 
# 
# -1000 <= a, b <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ba = bin(a)[2: ]
        bb = bin(b)[2: ]
        ba, bb = self.align(ba, bb)

        up = '0'
        res = []
        for x, y in zip(reversed(ba),reversed(bb)):
            up, r = self.add(x, y, up)
            res.append(r)
        res.append(up)

        bc = ''.join(reversed(res))
        return int(bc, base=2)

    def add(self, b1, b2, up):
        """
        b1+b2
        """
        if b1==b2:
            return b1, up
        elif b1!=b2:
            if up=='1':
                return '1', '0'
            if up=='0':
                return '0','1'

    def minus(self, b1, b2, up):
        """
        b1-b2
        """
        if b1==b2:
            return up, '0'
        else:
            if b1=='1':
                return '0','1' if up=='0' else '0','0'
            else:
                return '1', up

    def align(self, s1, s2):
        itv = abs(len(s1)-len(s2))
        if len(s1) < len(s2):
            s1 = '0'*itv + s1
        elif len(s1) > len(s2):
            s2 = '0'*itv + s2
        return s1, s2
# @lc code=end
so = Solution()

print(so.getSum(3,2))
