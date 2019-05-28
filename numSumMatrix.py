class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.lrow = len(matrix)
        if self.lrow == 0:
            self.dp = [[]]
            return
        self.lcol = len(matrix[0])
        self.dp = [[0 for _ in range(self.lcol)] for _ in range(self.lrow)]
        for i in range(self.lrow):
            for j in range(self.lcol):
                self.dp[i][j] = self.dp[i][j-1] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r = 0
        for row in range(row1, row2+1):
            if col1 == 0:
                r += self.dp[row][col2]
            else:
                r += self.dp[row][col2] - self.dp[row][col1-1]
        return r
                
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)