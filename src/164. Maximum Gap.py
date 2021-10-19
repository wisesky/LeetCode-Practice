from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0

        nums.sort()

        gap = float('-inf')
        for i in range(1, length):
            gap = max(gap, nums[i]-nums[i-1])
        return gap

nums = [3,6,9,1]

so = Solution()
print(so.maximumGap(nums))
        
