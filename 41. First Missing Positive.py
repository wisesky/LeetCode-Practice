from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i


if __name__ == "__main__":
    nums = [1,2,0]
    nums = [3,4,-1,1]
    nums = [7,8,9,11,12]
    so = Solution()
    res = so.firstMissingPositive(nums)
    print(res)
                