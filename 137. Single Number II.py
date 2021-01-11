from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        # if length <= 3:
        #     pass

        nums.sort()
        for i in range(0, length-2, 3):
            if len(set(nums[i:i+3])) > 1:
                return nums[i]

        return nums[-1]


nums = [2,2,3,2]
nums = [0,1,0,1,0,1,99]

so = Solution()
print(so.singleNumber(nums))