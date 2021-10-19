from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        st = 0
        ed = len(nums) - 1
        # mid = (st+ed) // 2
        while st <= ed:
            mid = (st+ed) // 2
            midVal = nums[mid]
            # print('mid ', mid,midVal)
            if midVal == target:
                return mid
            elif midVal > target:
                ed = mid - 1
            else:
                st = mid + 1
            
        return st

if __name__ == "__main__":
    so = Solution()
    nums = [1,3,5,6]
    print(so.searchInsert(nums, 0))