#
# @lc app=leetcode id=1825 lang=python3
#
# [1825] Finding MK Average
#
# https://leetcode.com/problems/finding-mk-average/description/
#
# algorithms
# Hard (28.68%)
# Likes:    136
# Dislikes: 71
# Total Accepted:    4.4K
# Total Submissions: 14.9K
# Testcase Example:  '["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage","addElement","addElement","addElement","calculateMKAverage"]\n' +
  # '[[3,1],[3],[1],[],[10],[],[5],[5],[5],[]]'
#
# You are given two integers, m and k, and a stream of integers. You are tasked
# to implement a data structure that calculates the MKAverage for the stream.
# 
# The MKAverage can be calculated using these steps:
# 
# 
# If the number of the elements in the stream is less than m you should
# consider the MKAverage to be -1. Otherwise, copy the last m elements of the
# stream to a separate container.
# Remove the smallest k elements and the largest k elements from the
# container.
# Calculate the average value for the rest of the elements rounded down to the
# nearest integer.
# 
# 
# Implement the MKAverage class:
# 
# 
# MKAverage(int m, int k) Initializes the MKAverage object with an empty stream
# and the two integers m and k.
# void addElement(int num) Inserts a new element num into the stream.
# int calculateMKAverage() Calculates and returns the MKAverage for the current
# stream rounded down to the nearest integer.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement",
# "calculateMKAverage", "addElement", "addElement", "addElement",
# "calculateMKAverage"]
# [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
# Output
# [null, null, null, -1, null, 3, null, null, null, 5]
# 
# Explanation
# MKAverage obj = new MKAverage(3, 1); 
# obj.addElement(3);        // current elements are [3]
# obj.addElement(1);        // current elements are [3,1]
# obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements
# exist.
# obj.addElement(10);       // current elements are [3,1,10]
# obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
# ⁠                         // After removing smallest and largest 1 element
# the container will be [3].
# ⁠                         // The average of [3] equals 3/1 = 3, return 3
# obj.addElement(5);        // current elements are [3,1,10,5]
# obj.addElement(5);        // current elements are [3,1,10,5,5]
# obj.addElement(5);        // current elements are [3,1,10,5,5,5]
# obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
# ⁠                         // After removing smallest and largest 1 element
# the container will be [5].
# ⁠                         // The average of [5] equals 5/1 = 5, return 5
# 
# 
# 
# Constraints:
# 
# 
# 3 <= m <= 10^5
# 1 <= k*2 < m
# 1 <= num <= 10^5
# At most 10^5 calls will be made to addElement and calculateMKAverage.
# 
# 
#
from sortedcontainers import SortedList, sortedlist
from collections import deque
# @lc code=start
from sortedcontainers import SortedList
# class MKAverage:
#   """
#   TLE: O(mlogm) in calculateMKAverage
#   需要将 calculatedMKAverage 优化
#   """
#   def __init__(self, m: int, k: int):
#       self.k = k
#       self.m = m
#       self.nums = SortedList()
#       self.windows = deque()

#   def addElement(self, num: int) -> None:
#     """
#     O(logm)
#     """
#     if len(self.nums) == self.m:
#       val = self.windows.popleft()
#       self.nums.remove(val)
      
#     self.nums.add(num)
#     self.windows.append(num)
        
#   def calculateMKAverage(self) -> int:
#     """
#     O(mlogm)
#     由于 SortedList.__getitem__() : O(logn)
#     所以 SortedList[k:-k] : O(nlogn)
#     这也是 TLE 的主要原因
#     """
#     length = len(self.nums)
#     if length < self.m:
#       return -1

#     return sum(self.nums[self.k:-self.k]) // (self.m-2*self.k)

class MKAverage:
  """
  将 window 划分为: fisrt_k, mid, last_k
  并在 addElement 中不断更新 上述三段区域的 sum
  达到维持 O(logm) 的同时，把 calculateAvg 降到 O(1)
  维持 first_k , mid, last_k 只需要关注 add, delete 2个操作
  mid 和 all 中的值 只需要更新其中一个即可， 考虑到 all 更新简单一点，选择更新 all 的值

  add: 根据 num in SortedList 中的index 是否在 first_k, last_k 中，
      增加 num 并且 删除被挤出 first_k , last_k 中的值，
      注意在初始化的时候， first_k , last_k 会用窗口重合的部分

  delete: 当 len(windows) == m 的时候，需要删除 窗口 first 中的 val， 
          并在 first_k, last_k , all 中 根据 val 在 SortedList 中的index 更新值

  """
  def __init__(self, m, k):
    self.m = m
    self.k = k
    self.nums = SortedList()
    self.windows = deque()
    # all - first_k - last_k -> mid
    self.first_k = 0
    self.all = 0
    self.last_k = 0

  def addElement(self, num):
    """
    O(logm)
    alert off-by-1 error
    """
    length = len(self.windows)
    # bisect_left 寻找插入的位置
    pos = self.nums.bisect_left(num)
    self.all += num
    if pos < self.k:
      self.first_k += num
      if length >= self.k:
        self.first_k -= self.nums[self.k - 1]
    # 注意： 此处不能用 elif ，因为 初始化的时候， first_k , last_k 会有重合部分
    #  所以需要同时更新
    # elif pos > length - self.k:
    if pos > length - self.k:
      self.last_k += num
      if length >= self.k:
        self.last_k -= self.nums[-self.k]

    self.nums.add(num)
    self.windows.append(num)
    
    if length >= self.m:
      val = self.windows.popleft()
      val_pos = self.nums.index(val)
      self.nums.remove(val)
      self.all -= val
      if val_pos < self.k:
        self.first_k -= val
        # off-by-1 alert
        # nums.remove(val) 在前面， 要添加的是 nums[k-1]
        # nums.remove(val) 在后面， 要添加的是 nums[k]
        self.first_k += self.nums[self.k-1]
      elif val_pos > length - self.k:
        self.last_k -= val
        # off-by-1 alert
        # nums.remove(val) 在前面， nums[-k]
        # nums.remove(val) 在后面, nums[-k-1]
        self.last_k += self.nums[-self.k]
      # self.nums.remove(val)

  def calculateMKAverage(self):
    if len(self.windows) < self.m:
      return -1

    return (self.all - self.first_k - self.last_k) // (self.m - 2*self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
# @lc code=end

obj = MKAverage(3, 1)
obj.addElement(3)
obj.addElement(1)
print(obj.calculateMKAverage())
obj.addElement(10)
print(obj.calculateMKAverage())
obj.addElement(5)
obj.addElement(5)
obj.addElement(5)
print(obj.calculateMKAverage())