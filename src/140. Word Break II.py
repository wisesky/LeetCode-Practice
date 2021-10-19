from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        length = len(s)
        if length == 0:
            return []
        set_words = set(wordDict)
        set_words.update('')
        dp = [True] + [False] * length # dp[i] mean s[ :i] can split in wordDict
        bp = [[]for _ in range(length+1)]
        for i in range(length+1):
            for j in range(i):
                if dp[j] and s[j:i] in set_words:
                    dp[i] = True
                    bp[i].append(j)
                    # break

        # return dp[-1]
        # return bp[-1]
        result = []
        self.backRestore(bp, s, [[]], length, result)
        result = [' '.join(r) for r in result]
        return result

    def backRestore(self, bp, s, res, st, result):
        if st == 0:
            result.extend(res)
            return 
        
        for ed in bp[st]:
            sub = s[ed:st]
            newRes = [[sub]+r for r in res]
            self.backRestore(bp, s,newRes, ed, result)
        return


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

so = Solution()
print(so.wordBreak(s, wordDict))