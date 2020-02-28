class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0 for _ in range(n+1)]
        f[1] = 1
        #f[2] = 2
        for i in range(2,n+1):
            r = 0
            for k in range(i+1):
                if k == 0:
                    r += f[i-1]
                    
                elif k == i:
                    r += f[i-1]
                else:
                    r += f[k] * f[i-k-1]
            f[i] = r
        #print(f)
        return f[n]