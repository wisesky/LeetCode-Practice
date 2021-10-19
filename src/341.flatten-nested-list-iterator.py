#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (57.13%)
# Likes:    2644
# Dislikes: 923
# Total Accepted:    250.2K
# Total Submissions: 437.9K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# You are given a nested list of integers nestedList. Each element is either an
# integer or a list whose elements may also be integers or other lists.
# Implement an iterator to flatten it.
# 
# Implement the NestedIterator class:
# 
# 
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with
# the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean _hasNext() Returns true if there are still some integers in the nested
# list and false otherwise.
# 
# 
# Your code will be tested with the following pseudocode:
# 
# 
# initialize iterator with nestedList
# res = []
# while iterator._hasNext()
# ⁠   append iterator.next() to the end of res
# return res
# 
# 
# If res matches the expected flattened list, then your code will be judged as
# correct.
# 
# 
# Example 1:
# 
# 
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until _hasNext returns false, the
# order of elements returned by next should be: [1,1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until _hasNext returns false, the
# order of elements returned by next should be: [1,4,6].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-10^6, 10^6].
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator(object):
    """
    Not PASS
    """
    def __init__(self, nestedList ):
        self.iter = iter(nestedList)
        self._hasNext = None
        self.crt = None
    
    def next(self) -> int:
        """
        _hasNext : None 还未确定是否拥有next，直接调用next(iter)
            False raise StopIteration error，可通过next(iter) raise相同的错误
                True 已经缓存在 self.next 中    
        """
        if self.crt is not None :
            if self.crt.hasNext():
                return self.crt.next()
            else:
                self.crt = None

        if self._hasNext: 
            r = self.nextval
        else: # None or False
            r = next(self.iter)
        self._hasNext = None
        
        if isinstance(r, list):
            self.crt = NestedIterator(r)
            if self.crt.hasNext():
                return self.crt.next()
        elif isinstance(r, int):
            return r
    
    def hasNext(self) -> bool:
        """
        _hasNext : None -> True/False
        """
        if self.crt is not None :
            if self.crt.hasNext():
                return True
            else:
                self.crt = None

        if self._hasNext is None:
            try:
                self.nextval = next(self.iter)
            except StopIteration:
                self._hasNext = False
            else:
                self._hasNext = True
        return self._hasNext


class NestedIterator(object):
    """
    stack 存储li逆序, stack.pop() 判断是 integer or List, integer 返回 int， List 则合并在 stack中
     重要的是这个过程是在 next 还是 hasNext 中， 根据调用用例， 每次 hasNext 必首先调用，所以在 hasNext 中进行相关操作
    """
    def __init__(self, li) -> None:
        self.stack = li[ : :-1]
    
    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            first = self.stack[-1]
            if first.isInteger():
                return True
            # self.stack = self.stack[ :-1] + first.getList()[ : :-1]
            self.stack.extend(self.stack.pop().getList()[ : :-1])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

i, v =NestedIterator([1,[4,[6]]]), []
while i.hasNext():
    v.append(i.next())
print(v)