import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [float('inf') for _ in range(n+1)]
        d[0] = 0
        #d[1] = 1
        e = []
        for i in range(1, int(n**0.5 + 1)):
            ins = i*i
            e.append(ins)
            d[ins] = 1
        def dp(num):
            if d[num] != float('inf'):
                return d[num]
            #pos = biSearch(e, n)
            pos = int(num**0.5)
            #mi = float('inf')
            for k in e[ :pos]:
                d[num] = min(d[num] , dp(num-k) + 1)
            #d[n] = mi + 1
            return d[num]
        return dp(n)
         