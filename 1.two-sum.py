from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution 1
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i, j]
        # solution 2
        d = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if d.get(res) != None:
                return [d.get(res), i]
            d[nums[i]] = i
        return False

if __name__ == "__main__":
    so = Solution()
    nums = [2,7,11,15]
    target = 13
    nums = [3,2,4]
    target = 6
    nums = [3,3]
    target = 6
    res = so.twoSum(nums, target)
    print(res)