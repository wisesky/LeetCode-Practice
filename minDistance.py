class Solution:
    # edit distance
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        
        l = l1 if l1 >= l2 else l2
    #    lc = lcs(word1, word2)
        
    #def lcs(s1, s2):
        dp = []
       # dp[i][j] 表示 从i 到j 需要转换的次数
        # dp[i][0] = i dp[0][j] = j
        for i in range(l1 + 1):
            dp.append([i])
        for j in range(1,l2+1):
            dp[0].append(j)

        for i in range(1,l1+1):

            for j in range(1,l2+1):
                x = i - 1
                y = j - 1
                # w1[x] == w2[y] 即不用转换
                if word1[x] == word2[y]:
                    dp[i].append(dp[x][y])
                else:
                    # 若不相等， 则分三种情况：
                    # d[i-1][j-1] + 1 : replace
                    # d[i-1][j] + 1 ： w1(i-1) --> w2(j) 的次数 +  删除 w1[i] 这一个字符的次数即 1
                    # d[i][j-1] + 1: w1[i] --> w2[j-1] 的次数 + insert w2[j] 这一个自负电次数 即 1 
                    tmp = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    dp[i].append(tmp + 1)
        #return dp[i][j]
        return dp[-1][-1]

