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
            # 每当i += 1 就是再之前的 2**i 个的基础上 多一个 1
            # eg: 0:0     10:1
            #     1:1 =>  11:2
            # eg: 0:0         110: 1
            #     1:1    =>   101: 2
            #     10:1        110:2 
            #     11:2        111:3

            interval = 2**i
            for j in range(interval):
                dp.append(dp[j] + 1)
            #print(i, len(dp))
            i += 1
        return dp[ :num+1]

