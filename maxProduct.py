import math
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma = []
        mi = []
        for i, num in enumerate(nums):
            if i is 0:
                ma.append(num)
                mi.append(num)
            r1 = ma[-1] * num
            r2 = mi[-1] * num
            ma.append(max(r1,r2, num))
            mi.append(min(r1,r2, num))
        print(ma)
        print(mi)
        return max(ma)
                    
            
