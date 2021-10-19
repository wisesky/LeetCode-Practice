from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        half_length = len(nums) // 2
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > half_length:
                return num

nums = [1,1,1,1,2,2,2]

so = Solution()
r = so.majorityElement(nums)
print(r)