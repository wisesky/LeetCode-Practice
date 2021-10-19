from typing import Dict, List

class Solution:
    # s1: DFS TLE
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(set(s)) > len(set(''.join(wordDict))):
            return False
        set_words = set(wordDict)
        r = self.helper(s, set_words)
        return r

    def helper(self, s, set_words):
        if s in set_words:
            return True

        for i in range(len(s),0,-1):
            sub = s[ :i]
            if sub in set_words:
                if  self.helper(s[i: ], set_words):
                    return True

        return False

    # s2 DP passed
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        if length == 0:
            return False
        set_words = set(wordDict)
        set_words.update('')
        dp = [True] + [False] * length # dp[i] mean s[ :i] can split in wordDict

        for i in range(length+1):
            for j in range(i):
                if dp[j] and s[j:i] in set_words:
                    dp[i] = True
                    break

        return dp[-1]

s = "leetcode"
wordDict = ["leet", "code"]
s = "applepenapple"
wordDict = ["apple", "pen"]
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

so = Solution()
print(so.wordBreak(s, wordDict))