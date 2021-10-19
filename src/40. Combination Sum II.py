from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        flag, res = self.resCombintion(candidates, target)
        if flag:
            return res
        else:
            return []

    def resCombintion(self, nums, resSum):
        if len(nums) == 0:
            return False, None
        if nums[0] > resSum:
            return False, None

        res = []
        for i, num in enumerate(nums):
            if num == resSum:
                res.append([num])
                continue
            flag, r = self.resCombintion(nums[i+1: ], resSum-num)
            if flag :
                r = [[num] + x for x in r]
                res.extend(r)
        
        if len(res) > 0:
            tmp = []
            for t in res:
                if t not in tmp:
                    tmp.append(t)
            return True, tmp
        else:
            return False, None

if __name__ == "__main__":
    so = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    candidates = [2,5,2,1,2]
    target = 5
    res = so.combinationSum2(candidates, target)
    print(res)