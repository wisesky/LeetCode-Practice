#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (38.66%)
# Likes:    2088
# Dislikes: 239
# Total Accepted:    269.7K
# Total Submissions: 695.9K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
# 
# 
# Example 1:
# 
# 
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lower-case English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
# 
# 
#

# @lc code=start
from typing import Pattern


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2word = {}
        word2p = {}
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        for p,word in zip(pattern, words):
            if p in p2word:
                if p2word[p] != word:
                    return False
            else:
                if word in word2p:
                    return False
                p2word[p] = word
                word2p[word] = p
        else:
            return True
# @lc code=end

pattern = 'abba'
s = 'dog dog dog dog'
pattern = 'aaa'
s = 'aa aa aa aa'

so = Solution()
print(so.wordPattern(pattern, s))