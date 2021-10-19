from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted(nums) 
        res = []               
        for i,num in enumerate(nums):
            lo = i+1
            hi = len(nums-1)
            sm = 0 - num

            while(lo < hi):
                if nums[lo] + nums[hi] == sm:
                    res.append([num, nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1

                elif nums[lo] + nums[hi] < sm:
                    lo += 1
                else:
                    hi -= 1
                
        return res
