from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        marked = [False for _ in range(length)]

        result = self.helper(nums, marked)

        newRes = []
        for r in result :
            if r not in newRes:
                newRes.append(r) 
        return newRes

    def helper(self, nums, marked):
        length = len(nums)
        if length == 0:
            return [[]]
        
        if length == 1:
            return [nums]

        result = []
        for i,num in enumerate(nums):
            if  not marked[i] :
                marked[i] = True
                r = self.helper(nums, marked)
                marked[i] = False
                # res = [[num]+x for x in r]
                res = []
                for x in r:
                    newX = [num] + x
                    if newX not in res:
                        res.append(newX)
                result.extend(res)

        return result if len(result) > 0 else  [[]]

if __name__ == "__main__":
    nums = [1,1,3]

    so = Solution()
    result = so.permuteUnique(nums)
    print(result)    
    
