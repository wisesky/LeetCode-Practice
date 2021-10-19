from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        pre = float('-inf')
        post = float('inf')
        length = len(nums)
        if length == 0:
            return 0

        for i in range(length):
            head = nums[i]
            tail = nums[-i]
            if head < pre:
                return head
            if tail > post :
                return post
            pre = head
            post = tail
        return nums[-1]
        
nums = [3,4,5,1,2]
nums = [11,13,15,17]
nums = [1]
so = Solution()
print(so.findMin(nums))
