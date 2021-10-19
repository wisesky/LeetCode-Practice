from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return

        # 找到nums[i] < max(nums[i+1: ])
        # s1
        # for i in range(len(nums)-2, -1, -1):
        #     if nums[i] < nums[i+1]:
        #         break
        # s2
        leftMax = float('-inf')
        for i in range(len(nums)-1, -1,-1):
            if nums[i] < leftMax:
                break
            else:
                leftMax = nums[i]

        if i == 0 and nums[i] >= nums[i+1]:
            nums.reverse()
            return

        d = {}
        flag = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] > flag:
                d[j] = nums[j] - flag

        sd = sorted(d.items(), key=lambda x: (x[1], -x[0]))
        j, _ = sd[0]

        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp
        # print(i, j )
        nums[i+1: ] = sorted(nums[i+1: ])
        
        return

if __name__ == "__main__":
    so = Solution()
    # nums = [2,3,1]
    # nums = [1,3,2]
    nums = [1,2,3]
    so.nextPermutation(nums)
    print(nums)