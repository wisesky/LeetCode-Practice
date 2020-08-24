class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
        br = [[0 for _ in range(col)] for _ in range(row)]
        bc = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    #dp[i,j] = 1
                    br[i][j] = br[i][j-1] + 1
                    bc[i][j] = bc[i-1][j] + 1
                    if br[i][j] >dp[i][j] and bc[i][j] >dp[i][j]:
                        dp[i+1][j+1] = dp[i][j] + 1
                    elif dp[i][j] >= min(br[i][j], bc[i][j]):
                        dp[i+1][j+1] = min(br[i][j], bc[i][j])
                    else:
                        # print('other case : 1')
                        dp[i+1][j+1] = 1
        r = 0
        for x in dp:
            for y in x:
                r = max(r, y)
        return r**2

if __name__ == "__main__":
    
    matrix = [
        [1,0,1,0,0],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0],
    ]

    matrix = [[str(z) for z in y] for y in matrix]

    so = Solution()
    print(so.maximalSquare(matrix))