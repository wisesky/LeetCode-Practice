from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = len(matrix)
        if l1 == 0:
            return False
        l2 = len(matrix[0])
        if l2 == 0:
            return False

        # flag = False
        for i in range(l1):
            nums = matrix[i]
            if nums[0] <= target and nums[-1] >= target:
                if self.binSearch(nums, target):
                    return True
        return False

    def binSearch(self, nums, target):
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mid = (lo+hi) // 2
            numMid = nums[mid]
            if numMid > target:
                hi = mid - 1
            elif numMid < target:
                lo = mid + 1
            else:
                return True
        return False

if __name__ == "__main__":
    so = Solution()
    matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    target = 3

    matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    target = 13

    res = so.searchMatrix(matrix, target)
    print(res)

                
