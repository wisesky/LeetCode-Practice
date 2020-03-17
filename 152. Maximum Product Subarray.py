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
                continue
            r1 = ma[-1] * num
            r2 = mi[-1] * num
            ma.append(max(r1,r2, num))
            mi.append(min(r1,r2, num))
        print(ma)
        print(mi)
        return max(ma)
                    

if __name__ == "__main__":
    so = Solution()
    l = [-2,0,-1]
    l = [2,3,-2,4]
    print(so.maxProduct(l))
            
