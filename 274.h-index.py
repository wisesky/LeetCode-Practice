#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (36.63%)
# Likes:    978
# Dislikes: 1578
# Total Accepted:    209.1K
# Total Submissions: 569.5K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their i^th paper, return compute the
# researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: A scientist has an index
# h if h of their n papers have at least h citations each, and the other n − h
# papers have no more than h citations each.
# 
# If there are several possible values for h, the maximum one is taken as the
# h-index.
# 
# 
# Example 1:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining two with no more than 3 citations each, their h-index is 3.
# 
# 
# Example 2:
# 
# 
# Input: citations = [1,3,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        逆排序 数组， 分别有 引用次数递减序列 和 大于等于当前引用次数递增序列
        more:     1,2,3,4,5 递增
        citation: 6,5,3,1,0 递减
        第一次出现 more > citaiton 的指针的前一个 more 即所求
        最后，遍历所有 citaitons 仍然未出现more>citaiton的终止条件，
        那么当前的more即所求，相当于citations的末尾就是 终止条件，
        """
        citations.sort(reverse=True)
        for i in range(len(citations)):
            more = i+1
            citation = citations[i]
            if more > citation:
                return i # more-1
        return more
# @lc code=end

so = Solution()
nums = [1,2,3,4,5,6,7,8]
# nums = [100]
nums = [0,0,4,4]
# nums = [0,1,3,5,6]
nums = [1,7,9 ,4]
print(so.hIndex(nums))