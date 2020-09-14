from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i, num in enumerate(nums):
            res = result.copy()
            for r in res:
                result.append(r+[num])

        return result

if __name__=='__main__':
    so = Solution()
    nums = [1,2,3]
    res = so.subsets(nums)
    print(res)