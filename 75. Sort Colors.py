from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick3Way(nums, 0, len(nums)-1)
        
    def quick3Way(self, nums, lo, hi):
        if lo >= hi:
            return
        
        lt = lo
        # 原版algs4 中的三相快排 此处: i = lo + 1
        # 是因为吧 nums[0] 作为三相快排的 比较初值 v
        # 这里 初值已经预先指定为： 1 
        # 所以 i = lo
        i = lo 
        gt = hi
        while i <= gt:
            if nums[i] < 1:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1
            elif nums[i] > 1:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else: # nums[i] == 1
                i += 1
        return

if __name__ == "__main__":
    so = Solution()
    nums = [2,0,2,1,1,0,1,2,1,2,1,2,2,2]
    so.sortColors(nums)
    print(nums)