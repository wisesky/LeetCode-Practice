class Solution:
    # DFS
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) == 0:
            return 1
        if len(s) == 0:
            return 0
        if s == t:
            return 1

        r = 0
        t0 = t[0]
        pos = -1
        news = s[pos+1: ]
        while t0 in news:
            pos = news.index(t0)
            news = news[pos+1: ]
            r += self.numDistinct(news, t[1: ])
        return r

    # dp
    def numDistinct(self, s, t):
        dp = [0]* len(s)
        for i,char in enumerate(s):
            if char == t[0]:
                dp[i] = 1

        for char in t[1: ]:
            count = 0
            dp_next = [0] * len(s)
            for i in range(len(s)):
                if s[i] == char:
                    dp_next[i] = count
                count += dp[i]
            dp = dp_next

        return sum(dp)

    

so = Solution()

s = 'rabbbit'
t = 'rabbit'
s = "babgbag"
t = "bag"
res = so.numDistinct(s, t)
print(res)
        