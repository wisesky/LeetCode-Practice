from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return matrix

        for i in range(n-1, -1, -1):
            nums = matrix[i]
            pos = n - i - 1
            for j,num in enumerate(nums[pos: ]):
                matrix[j].insert(pos, num)
            matrix[i] = matrix[i][ :pos+1]

        # for i in range(n):
        #     matrix[i] = matrix[i][ :n]

        return matrix

if __name__ == "__main__":
    matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
    matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    
    so = Solution()
    res = so.rotate(matrix)
    print(res)
        