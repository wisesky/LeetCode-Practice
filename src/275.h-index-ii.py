#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (36.51%)
# Likes:    579
# Dislikes: 907
# Total Accepted:    146.3K
# Total Submissions: 400.1K
# Testcase Example:  '[0,1,3,5,6]'
#
# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their i^th paper and citations is sorted
# in an ascending order, return compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: A scientist has an index
# h if h of their n papers have at least h citations each, and the other n − h
# papers have no more than h citations each.
# 
# If there are several possible values for h, the maximum one is taken as the
# h-index.
# 
# You must write an algorithm that runs in logarithmic time.
# 
# 
# Example 1:
# 
# 
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
# of them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining two with no more than 3 citations each, their h-index is 3.
# 
# 
# Example 2:
# 
# 
# Input: citations = [1,2,100]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# n == citations.length
# 1 <= n <= 10^5
# 0 <= citations[i] <= 1000
# citations is sorted in ascending order.
# 
# 
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        见 274 hIndex_1
        """
        length = len(citations)
        for i in range(length):
            j = length - i - 1 # or -(i+1)
            more = i + 1
            citation = citations[j]
            if more > citation:
                return i # more-1
        return more
# @lc code=end

