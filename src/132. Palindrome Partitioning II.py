class Solution:
    # s1 TLE
    def minCut(self, s: str) -> int:
        memo = {}
        r = self.splitPalindrome(s, memo)
        return r - 1
    
    def splitPalindrome(self, s, memo):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        res = float('inf')
        for i in range(len(s), 0,-1):
            if self.isPalindrome(s[ :i], memo):
                # r = self.splitPalindrome(s[i: ], memo)
                # if r < float('inf'):
                #     return r + 1
                res = min(res, 1 + self.splitPalindrome(s[i: ], memo))
        return res

    def isPalindrome(self, s, memo):
        if len(s) == 0:
            return False
        if len(s) == 1:
            return True

        if s in memo:
            return memo[s]

        if len(s) % 2 == 0:
            post = len(s) // 2
            pre = post - 1
        else:
            pre = len(s)//2 - 1
            post = len(s) // 2 + 1
        
        while pre >= 0 and post < len(s) and s[pre] == s[post]:
            pre -= 1
            post += 1
        
        if pre >= 0 and post < len(s):
            memo[s] = False
            return False
        memo[s] = True
        return True

    # s2  try dp
    def minCut(self, s: str) -> int:
        length = len(s)
        memo = [[0]*length for _ in range(length)]
        dp = self.longestPalindrome(s)
        self.calLength(0, s, dp, memo)
        return memo[0][-1] - 1
        # dp_2 = self.calLength(s, dp)
        # return dp_2[0][-1]

    # s2-1 自顶向下 备忘录dp AC 456ms
    def calLength(self, start, s, dp, memo):
        if start == len(s):
            return 0
        if start == len(s)-1:
            memo[start][len(s)-1] = 1
            return 1
        if dp[start][len(s)-1]:
            memo[start][len(s)-1] = 1
            return 1
        if memo[start][len(s)-1] != 0:
            return memo[start][len(s)-1]

        res = float('inf')
        for i in range(start, len(s)):
            if dp[start][i] :
                res = min(res, self.calLength(i+1, s, dp , memo))
        memo[start][len(s)-1] = res + 1
        return memo[start][len(s)-1]

    # s2-2 自底向上 dp TLE 
    def calLength(self, s, dp ):
        length = len(s)
        dp_2 = [[0]*length for _ in range(length)]
        if dp[0][length-1]:
            dp_2[0][-1] = 0
            return dp_2
        # s1 gap dp
        for gap in range(1, length):
            for i in range(length-gap):
                j = i+gap
                if not dp[i][j]:
                    r = float('inf')
                    for k in range(i, j):
                        r = min(r, dp_2[i][k] + dp_2[k+1][j] + 1)
                    
                    dp_2[i][j] = r

        return dp_2

    # dp 求substring 上三角是否是 回文字符 AC 456ms
    def longestPalindrome(self, s):
        length = len(s)
        dp = [[False]*length for _ in range(length)]
        for i in range(length):
            j = i
            while j >= 0:
                if s[j] == s[i] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = True
                j -= 1

        return dp

    # 普通 O(N**2) 解法 AC 568ms
    def longestPalindrome(self, s):
        length = len(s)
        d = [[False]*length for _ in range(length)]

        news = '_'.join(s)
        for i in range(len(news)):
            d[i//2][i//2] = True
            end = min(i, len(news)-i)
            flag = True
            for j in range(1,end+1):
                pre = i-j
                post = i+j
                
                if news[pre] != '_' and  flag:
                    if  news[pre] == news[post]:
                        d[pre//2][post//2] = True
                    else:
                        flag = False

        return d



s = 'aab'
s = 'a'
# s = 'ab'
# s = "ababababababababababababcbabababababababababababa"
# s = 'aaabaa'
# s = 'leet'
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
so = Solution()
r = so.minCut(s)
print(r)
# r1 = so.longestPalindrome(s)
# r2 = so.longestPalindrome_1(s)
# for r in r1:
#     print(r)
# print('*'*30)
# for r in r2:
#     print(r)