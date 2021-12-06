#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (49.49%)
# Likes:    536
# Dislikes: 130
# Total Accepted:    46.1K
# Total Submissions: 92.8K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' +
  #'[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
# Given a data stream input of non-negative integers a1, a2, ..., an, summarize
# the numbers seen so far as a list of disjoint intervals.
# 
# Implement the SummaryRanges class:
# 
# 
# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int val) Adds the integer val to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream
# currently as a list of disjoint intervals [starti, endi].
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
# 
# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= val <= 10^4
# At most 3 * 10^4 calls will be made to addNum and getIntervals.
# 
# 
# 
# Follow up: What if there are lots of merges and the number of disjoint
# intervals is small compared to the size of the data stream?
# 
#
from typing import List
# @lc code=start
class SummaryRanges:
  """
  扫描一遍nums， 生成 intervals
  """
    def __init__(self):
        self.nums = []

    def addNum(self, val: int) -> None:
        self.nums.append(val)

    def getIntervals(self) -> List[List[int]]:
        self.nums.sort()
        r = []
        start, end = None, None
        for num in self.nums:
          if start is None:
            start, end = num, num
          elif end + 1 == num:
            end = num
          elif end == num :
            continue
          elif end + 1 != num:
            r.append([start, end])
            start, end = num, num
        else:
          r.append([start, end])
        return r


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

