from typing import List
import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        needUpdate = set()
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1

                post = num+1
                if post in d:
                    needUpdate.add(num)

        while len(needUpdate) > 0:
            num = max(needUpdate)
            needUpdate = needUpdate - set([num])
            self.cal(num, d)
            pre = num-1
            while pre in d:
                d[pre] = d[pre+1] + 1
                needUpdate = needUpdate - set([pre])
                pre = pre - 1

        return max(d.values())

    def cal(self, num, d):
        if num+1 not in d:
            return d[num]
            
        d[num] = self.cal(num+1, d) + 1
        return d[num]
        

nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
# nums = []

so = Solution()
r = so.longestConsecutive(nums)
print(r)

                