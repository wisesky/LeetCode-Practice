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
                a = max(dp[j], j)
                b = max(dp[i-j], i-j)
                r = max(r, a*b)
            dp[i] = r
        return max(dp)