#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (58.28%)
# Likes:    2410
# Dislikes: 129
# Total Accepted:    128.5K
# Total Submissions: 220.1K
# Testcase Example:  '"2-1-1"'
#
# Given a string expression of numbers and operators, return all possible
# results from computing all the different possible ways to group numbers and
# operators. You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# 
# Example 2:
# 
# 
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
# 
# 
# Constraints:
# 
# 
# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# 
# 
#
from typing import List
import re
# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        li = re.split(r'([+-/*])', expression)
        result = self.dfsCal(li)
        return result

    def dfsCal(self, li):
        if len(li) == 1:
            return [int(li[0])]
        if len(li) == 3:
            return [eval(''.join(li))]
        
        length = len(li)
        result = []
        for i in range(length):
            if li[i] in ['+', '-', '*']:
                res1 = self.dfsCal(li[ :i])
                res2 = self.dfsCal(li[i+1: ])
                res = [self.cal(r1,r2, li[i]) for r1 in res1 for r2 in res2]
                result.extend(res)
        return result

    def cal(self, r1, r2, ops):
        if ops=='+':
            return r1+r2
        if ops=='-':
            return r1-r2
        if ops=='*':
            return r1*r2
# @lc code=end
so = Solution()
exp = '1-2-3'
exp = '2-1-1'
exp = '2*3-4*5'
result = so.diffWaysToCompute(exp)
print(result)