#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (61.28%)
# Likes:    1992
# Dislikes: 67
# Total Accepted:    236.4K
# Total Submissions: 384.6K
# Testcase Example:  '3\n7'
#
# Find all valid combinations of k numbers that sum up to n such that the
# following conditions are true:
# 
# 
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# 
# 
# Return a list of all possible valid combinations. The list must not contain
# the same combination twice, and the combinations may be returned in any
# order.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# 
# 
# Example 3:
# 
# 
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is
# 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
# 
# 
# Example 4:
# 
# 
# Input: k = 3, n = 2
# Output: []
# Explanation: There are no valid combinations.
# 
# 
# Example 5:
# 
# 
# Input: k = 9, n = 45
# Output: [[1,2,3,4,5,6,7,8,9]]
# Explanation:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
# There are no other valid combinations.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= k <= 9
# 1 <= n <= 60
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # memo = {}
        result = self.helper(k, n,list(range(1,10)))
        return result

    def helper(self, k, n ,left):
        """
        left: 排序列出的未被使用的list 集合
        在left 中搜索 k 个 数组成的sum 为 n 的集合
        由于是combination， 所以可以保持 left 排序的情况下，
        可以按照顺序 DFS，可以保证 得到的结果list 不会重复
        因为返回的结果list 是以 left[i] 为头的 所有结果
        """
        if k==0 and n==0:
            return [[]]
        if k < 1 or n < 1:
            return []

        result = []
        for i,v in enumerate(left):
            if n >= v:
                r = self.helper(k-1, n-v, left[i+1: ])
                if len(r) == 0:
                    continue
                res = [[v]+x for x in r]
                result.extend(res)
        
        return result
        
# @lc code=end
if __name__ == "__main__":
    so = Solution()
    k = 3
    n = 7
    n = 9
    n = 2
    # k = 4
    # n = 1
    result = so.combinationSum3(k, n)
    print(result)
