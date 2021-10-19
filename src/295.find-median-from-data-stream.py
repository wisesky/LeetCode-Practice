#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (48.42%)
# Likes:    5006
# Dislikes: 88
# Total Accepted:    350.4K
# Total Submissions: 715.9K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  # '[[],[1],[2],[],[3],[]]'
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value and the median is the mean of the two
# middle values.
# 
# 
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# 
# 
# Implement the MedianFinder class:
# 
# 
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data
# structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10^-5 of the actual answer will be accepted.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# 
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 
# 
# 
# Constraints:
# 
# 
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling
# findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are in the range [0, 100], how would
# you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how
# would you optimize your solution?
# 
# 
#
import heapq
from io import RawIOBase

# @lc code=start
from sortedcontainers import SortedList
class MedianFinder:
  """
  SortedList Solution: 872 ms(20%) 35.9 MB(16.88%)
  """
  def __init__(self):
      """
      initialize your data structure here.
      """
      self.nums = SortedList()

  def addNum(self, num: int) -> None:
      self.nums.add(num)

  def findMedian(self) -> float:
      length = len(self.nums)
      mid = int(length//2)
      if length%2==0:
        return (self.nums[mid] + self.nums[mid-1])/2
      else:
        return self.nums[mid]

class MedianFinder:
  """
  Priority Queue Solution: 560 ms(30%) 35.8 MB(19%)
  将nums 分成2个集合，left , right 且只关心left_max, right_min
  因为mid 就在这2个值之间产生
  """
  def __init__(self):
    self.sz = 0
    self.left = []
    self.right = []

  def addNum(self, num):
    """
    需要判断 num 是在 left 还是 right 
    同时还要根据 left_length 和 right_length 来进行 length balance
    """
    self.sz += 1
    if len(self.left) == len(self.right):
      if len(self.left) == 0:
        heapq.heappush(self.left, -num)
        return
      # add left 无需 length balance
      if self.right[0] >= num:
        heapq.heappush(self.left, -num)
      # add right 需要 length balance
      else:
        val = heapq.heapreplace(self.right, num)
        heapq.heappush(self.left, -val)
    else: # length_left == length_right + 1
      # add right ,no length balance
      if num >= -self.left[0]:
        heapq.heappush(self.right, num)
      # add left, need length
      else:
        val = - heapq.heapreplace(self.left, -num)
        heapq.heappush(self.right, val)

  def findMedian(self):
    val = -self.left[0]
    if self.sz % 2 == 0:
      return (val+self.right[0]) / 2
    else:
      return val

class MedianFinder:
  """
  Priority Queue Optim Solution: 580 ms(28%) 36.8 MB(7%)
  优化 addNum 实现
  num -> left -> right
  同时每当 right_length > left_length 的时候，回退一个num
  """
  def __init__(self) -> None:
    self.left = []
    self.right = []
    
  def addNum(self, num):
    val = - heapq.heappushpop(self.left, -num)
    heapq.heappush(self.right, val)
    if len(self.left) < len(self.right):
      val = heapq.heappop(self.right)
      heapq.heappush(self.left, -val)

  def findMedian(self):
    return -self.left[0] if len(self.left) > len(self.right) \
            else (self.right[0]-self.left[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

obj = MedianFinder()
obj.addNum(-1)
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
# obj.addNum(10)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())