#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.43%)
# Likes:    6258
# Dislikes: 301
# Total Accepted:    697.7K
# Total Submissions: 1.1M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#
from typing import List
# @lc code=start
class Solution:
    # 118ms(40%) 18.8MB(60%)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1, 统计次数
        2，次数排序，去除 Topk 的次数
        3, 返回次数达标的num
        """
        num2count = {}
        for num in nums:
            if num in num2count:
                num2count[num] += 1
            else:
                num2count[num] = 1
        counts = list(num2count.values())
        counts.sort()
        threshold = counts[-k]
        r = [num for num, count in num2count.items() if count >= threshold]
        return r
# @lc code=end
so = Solution()

nums = [1,1,1,2,2,3,3,3]
k = 2

print(so.topKFrequent(nums, k))
