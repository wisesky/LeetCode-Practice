#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (42.00%)
# Likes:    4409
# Dislikes: 132
# Total Accepted:    197.5K
# Total Submissions: 469.9K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: nums = [-1,-1]
# Output: [0,0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    """
    6.1ms(8%) 29.6MB(98%)
    O(n**2 * logn)

    从nums 右-左遍历取数num， num 插入排序到li中，并返回插入的位置i
    此时插入的位置i就是当前num的r

    插入排序的Time Complexity O(nlogn)
    二分查找插入位置 O(logn)
    list.insert() O(n)
    如果有更优的插入的数据结构，如链表，insert -> O(1)
    那么可以降低最多一个 O(n)的复杂度
    """
    def countSmaller(self, nums: List[int]) -> List[int]:
        li = []
        res = []
        while len(nums) > 0:
            num = nums.pop()
            r = self.binSearchInsert(li, num)
            res.append(r)

        res.reverse()
        return res

    def binSearchInsert(self, li, val):
        """
        二分查找 已排序li中val的插入位置
        并插入 val
        """
        lo, hi = 0, len(li)
        while lo < hi:
            mid = lo + (hi-lo)//2
            if li[mid] < val:
                lo = mid + 1
            else:
                hi = mid
        
        li.insert(lo, val)
        return lo
            

# @lc code=end

so = Solution()

nums = [5,2,6,1]
nums = [-1]
nums = [-1,-1]
print(so.countSmaller(nums))