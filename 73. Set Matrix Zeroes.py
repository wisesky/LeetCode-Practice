from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRow, zeroCol = set(), set()

        l1 = len(matrix)
        if l1 == 0:
            return
        l2 = len(matrix[0])

        for i in range(l1):
            for j in range(l2):
                if matrix[i][j] == 0:
                    zeroRow.add(i)
                    zeroCol.add(j)
        
        self.zeroRowCol(matrix, zeroRow, zeroCol)
        return 

    def zeroRowCol(self, matrix, row, col):
        l1 = len(matrix)
        l2 = len(matrix[0])
        for i in row:
            matrix[i] = [0] * l2
        for j in col:
            for i in range(l1):
                matrix[i][j] = 0
        return

if __name__ == "__main__":
    so = Solution()
    matrix = [  [1,1,1],
                [1,0,1],
                [1,1,1]
                ]

    matrix = [  [0,1,2,0],
                [3,4,5,2],
                [1,3,1,5]
                ]  
    so.setZeroes(matrix)

    for m in matrix:
        print(m)