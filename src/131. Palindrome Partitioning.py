from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        memo = {}
        self.splitPalindrome(s, [], res, memo)
        return res
        
    def isPalindrome(self, s, memo):
        if len(s) == 0:
            return False
        if len(s) == 1:
            return True

        if s in memo:
            return memo[s]

        news = '_'.join(s)
        mid = len(news) // 2
        for i in range(1,mid+1):
            pre = mid - i
            post = mid + i 
            if news[pre] != news[post]:
                memo[s] = False
                return False
        memo[s] = True
        return True

    # no join
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

    def splitPalindrome(self, s, rs, res,memo):
        if len(s) == 0:
            res.append(rs)
            return
        if len(s) == 1:
            res.append(rs+[s])
            return

        for i in range(1,len(s)+1):
            if self.isPalindrome(s[ :i], memo):
                self.splitPalindrome(s[i: ], rs + [s[ :i]], res, memo)
        return

s = 'aab'
# s = 'a'
s = 'aabb'

so = Solution()
res = so.partition(s)
print(res)