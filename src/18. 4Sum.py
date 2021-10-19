from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums) 
        res = []               
        for i,num1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                lo = j+1
                hi = len(nums)-1
                sm = target - num1 - num2

                while(lo < hi):
                    if nums[lo] + nums[hi] == sm:
                        if [num1, num2, nums[lo], nums[hi]] not in res:
                            res.append([num1, num2, nums[lo], nums[hi]])
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

if __name__ == "__main__":
    so = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    res = so.fourSum(nums, target)
    print(res)
