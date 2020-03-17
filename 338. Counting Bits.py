import math
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]
        i = 0
        while 2**i  <= num:
            #le = 2**i
            interval = 2**i
            for j in range(interval):
                dp.append(dp[j] + 1)
            #print(i, len(dp))
            i += 1
        return dp[ :num+1]

