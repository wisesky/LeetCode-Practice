#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (55.43%)
# Likes:    1417
# Dislikes: 90
# Total Accepted:    132.3K
# Total Submissions: 237.5K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, return the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. If no such
# two words exist, return 0.
# 
# 
# Example 1:
# 
# 
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# 
# 
# Example 2:
# 
# 
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# 
# 
# Example 3:
# 
# 
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= words.length <= 1000
# 1 <= word_i.length <= 1000
# word_i consists only of lowercase English letters.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    """
    7.2s(5%) 14,6MB(65%)
    Time Complexity: O(n**2)
    遍历2遍得到 word_i, word_j 直接计算
    采用分桶的方式，过滤一些开头字母相同的words
    """
    def maxProduct(self, words: List[str]) -> int:
        head2word = {}
        for word in words:
            head = word[0]
            if head in head2word:
                head2word[head].append(word)
            else:
                head2word[head] = [word]
        
        res = 0
        for word_i in words:
            crtHead = word_i[0]
            for head, wordList in head2word.items():
                if crtHead == head:
                    continue
                for  word_j in wordList:
                    r = self.calVal(word_i, word_j)
                    res =max(res, r)

        return res

    def calVal(self, word_i, word_j):
        its = set(word_i) & set(word_j)    
        if len(its) > 0 :
            return 0

        return len(word_i) * len(word_j)
    # Useless
    def binSearch(self, words, letter):
        """
        words: 已排序 字符串 list
        从words 搜索 letter开头 的末尾+1的位置
        eg: 在words 搜索 a 开头的 word 结尾 + 1 的位置
        也就是 b 或者 c 等其他 只要 大于 a 的开头字母的位置
        """
        lo, hi = 0, len(words)
        while lo < hi:
            mid = lo + (hi-lo)//2
            if words[mid][0] <= letter:
                lo = mid + 1
            else:
                hi = mid
        return lo


# @lc code=end

