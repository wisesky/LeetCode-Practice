from operator import itemgetter
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        pre = float('inf')
        i_pre = -1
        count = 0
        r = []
        for i,num in enumerate(nums):
            if num == pre:
                count += 1
                if count == 2:
                    i_pre = i
            else:
                if count >= 2 and i_pre != -1:
                    # nums = nums[ :i_pre] + nums[i: ] 
                    r.append((i_pre, i))
                    
                pre = num    
                count = 0
                i_pre = -1

        if count >= 2 and i_pre != -1:
            # nums = nums[ :i_pre] + nums[i: ] 
            r.append((i_pre, length))

        itv = 0
        for st,ed in r:
            s = st - itv
            e = ed - itv
            for j in range(s, e):
                nums.pop(s)
            itv += e - s
        return len(nums)

if __name__ == "__main__":
    so = Solution()
    nums = [1,1,1,2,2,3]
    # nums = [0,0,1,1,1,1,2,2,2,3,3,3,3,3]
    res = so.removeDuplicates(nums)
    print(res)
    print(nums)
