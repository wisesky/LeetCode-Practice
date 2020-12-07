from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            val = nums2[i]
            self.insertOps(nums1, m+i, val)
        
        return

    def insertOps(self, nums,k, val):
        pos = self.findPos(nums[ :k], val)
        pre = val
        for i in range(pos, k+1):
            tmp = nums[i]
            nums[i] = pre
            pre = tmp
        return

    def findPos(self, nums, val):
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mid = (lo+hi) // 2
            mid_val = nums[mid]
            if mid_val == val:
                return mid
            elif mid_val > val:
                hi = mid - 1
            else: # mid_val < val
                lo = mid+1

        return lo


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

so = Solution()
so.merge(nums1, m, nums2, n)
print(nums1)
