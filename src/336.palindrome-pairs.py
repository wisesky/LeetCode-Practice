#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (36.18%)
# Likes:    2282
# Dislikes: 204
# Total Accepted:    136.5K
# Total Submissions: 377.4K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, return all the pairs of the distinct indices
# (i, j) in the given list, so that the concatenation of the two words words[i]
# + words[j] is a palindrome.
# 
# 
# Example 1:
# 
# 
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# Example 2:
# 
# 
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# 
# 
# Example 3:
# 
# 
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        baseline: 100/135 TLE
        分桶查询: 134/135 TLE
        """
        self.words = words
        tail2index =  {}
        for index, word in enumerate(words):
            if len(word) > 0 :
                tail = word[-1] 
                if tail in tail2index:
                    tail2index[tail].append(index)
                else:
                    tail2index[tail] = [index]

        res = []
        for i, word in enumerate(words):
            if len(word) > 0:
                head = word[0]
                for j in tail2index.get(head, []):
                    if i!=j and self.isPairs(i, j):
                        res.append([i,j])
            else:
                for j in range(len(words)):
                    if i!=j and self.isPairs(i, j):
                        res.append([i, j])
                        res.append([j, i])
        return res

    def isPairs(self, i, j):
        length = len(self.words[i]) + len(self.words[j])
        word = ''.join([self.words[i], self.words[j]])
        lo, hi = 0, length-1
        while lo <= hi:
            if word[lo] != word[hi]:
                return False
                # break
            lo += 1
            hi -= 1 

        return True

    # def palindromePairs(self, words):
    #     """
    #     manacher algs
    #     """
    #     self.words = words
    #     rls = []
    #     for i in range(len(words)):
    #         rl = self.rlOfWords(i)
    #         rls.append(rl)
        
    #     res = []
    #     for i in range(len(words)):
    #         for j in range(len(words)):
    #             if i!=j and self.isParisRls(i,j,rls):
    #                 res.append([i,j])    
    #     return res

    def isParisRls(self,i,j, rls):
        length_i = len(self.words[i])
        length_j = len(self.words[j])
        length = length_i + length_j 
        mid = length // 2
        if length % 2 == 0:
            left = 0
        else:
            left = 1

        if mid < length_i:
            rl = rls[i][2*mid+left]
            lo, hi = mid-rl+1, mid+rl-1
            if lo>0 and hi<length_i-1:
                return False
        else:
            mid_j = mid - length_i
            rl = rls[j][2*mid_j+left]
            lo, hi = mid_j-rl+1, mid+rl-1
            if lo>0 and hi<length_j-1:
                return False

        return self.isPairs(i, j)

    # def rlOfWords(self, word):
    #     word = '_'.join(word)
    def rlOfWords(self, i):
        word = '_'.join(self.words[i])
        
        word = '_' + word + '_'
        maxRight= -1
        pos = -1
        rl = [1] * len(word)
        for i in range(len(word)):
            # if i + rl[i] - 1 > maxRight:
            #     pass
            # else:
            if i <= maxRight:
                j = 2*pos-i
                # if rl[j]-1 < i-pos:
                if rl[j]-1 < maxRight-i:
                    rl[i] = rl[j]
                else:
                    rl[i] = maxRight-i+1
            # start from rl[i]
            lo,hi =  i-rl[i], i+rl[i]
            while lo>=0 and hi<len(word) and word[lo]==word[hi]:
                rl[i] += 1
                lo -= 1
                hi += 1

            if hi-1>maxRight:
                maxRight = hi
                pos = i
        return rl


# @lc code=end
so = Solution()

words = ["abcd","dcba","lls","s","sssll"]
# words = ['s','lls']
words = ["bat","tab","cat"]
# words = ["a",""]
# so.palindromePairs(words)
print(so.palindromePairs(words))
# print(so.rlOfWords('aba'))