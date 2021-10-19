from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        d2c = {}
        for num in nums:
            d2c[num] = d2c.get(num, 0) + 1

        res = [[]]
        for k in d2c:
            combs = self.comb(k , d2c[k])
            add = [r+c for r in res for c in combs]
            res.extend(add)
        
        # res.extend([ [] ])
        return res

    def comb(self, num, count):
        return [ [num]*c for c in range(1,count+1) ]


nums = [1,2,2]
so = Solution()
res = so.subsetsWithDup(nums)
print(res)