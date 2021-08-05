from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pre = float('-inf')
        length = len(nums)
        if length == 0:
            return -1

        ascd = False
        for i in range(length):
            cur = nums[i]
            if ascd and cur < pre:
                return i-1
            if not ascd and cur > pre:
                ascd = True
            pre = cur
        
        if ascd :
            return length-1
        else:
            return -1

nums = [1,2,1,3,5,6,4]

so = Solution()
print(so.findPeakElement(nums))