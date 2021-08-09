#
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#
# https://leetcode.com/problems/peeking-iterator/description/
#
# algorithms
# Medium (51.52%)
# Likes:    850
# Dislikes: 592
# Total Accepted:    141.1K
# Total Submissions: 272.3K
# Testcase Example:  '["PeekingIterator","next","peek","next","next","hasNext"]\n' +
  '[[[1,2,3]],[],[],[],[],[]]'
#
# Design an iterator that supports the peek operation on a list in addition to
# the hasNext and the next operations.
# 
# Implement the PeekingIterator class:
# 
# 
# PeekingIterator(int[] nums) Initializes the object with the given integer
# array nums.
# int next() Returns the next element in the array and moves the pointer to the
# next element.
# bool hasNext() Returns true if there are still elements in the array.
# int peek() Returns the next element in the array without moving the
# pointer.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 2, 2, 3, false]
# 
# Explanation
# PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
# peekingIterator.next();    // return 1, the pointer moves to the next element
# [1,2,3].
# peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
# peekingIterator.next();    // return 2, the pointer moves to the next element
# [1,2,3]
# peekingIterator.next();    // return 3, the pointer moves to the next element
# [1,2,3]
# peekingIterator.hasNext(); // return False
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# All the calls to next and peek are valid.
# At most 1000 calls will be made to next, hasNext, and peek.
# 
# 
# 
# Follow up: How would you extend your design to be generic and work with all
# types, not just integer?
#

# @lc code=start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

from collections import deque
from typing import Iterator


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        # self.vals = iterator.nums()
        self.vals = deque()
        while iterator.hasNext():
            self.vals.appendleft(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.vals[-1]

    def next(self):
        """
        :rtype: int
        """
        return self.vals.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.vals) != 0

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end

