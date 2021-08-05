from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if num in d:
                return [d[num], i+1]
            d[target-num] = i+1

nums = [2,7,11,15]
target = 9
nums = [2, 3,4]
target = 6
nums = [-1, 0]
target = -1

so = Solution()
print(so.twoSum(nums,target))