class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            r = 0
            for j in range(1, i):
                # dp[j] 代表j被拆分之后可以获得的最大乘积，并不包括j本身值，因为拆分次j和0， 乘积就是0
                a = max(dp[j], j)
                b = max(dp[i-j], i-j)
                r = max(r, a*b)
            dp[i] = r
        return max(dp)

if __name__ == "__main__":
    so = Solution()
    print(so.integerBreak(10))