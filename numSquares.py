class Solution:
    # OJ 脚本问题导致必须初始化为 class variable 
    # 而且 莫名其妙前面多了很多乱码数字 开始运行的时候len(self.dp)并不为1，
    dp = [0] # so now dp is a class variable
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        for i in range(len(self.dp),n+1):
            pos = int(i**0.5)
            if pos*pos == i:
                self.dp.append(1)
                continue
            mi = float('inf')
            for j in range(1,pos+1):
                #if i >= k:
             #   mi = min(mi,d[i-k])
                mi= min(mi, self.dp[i-j*j] + 1)
            self.dp.append(mi)
        return self.dp[n]
 