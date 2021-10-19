#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (42.02%)
# Likes:    1248
# Dislikes: 339
# Total Accepted:    212.8K
# Total Submissions: 506.3K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A',
# 'C', 'G', and 'T'.
# 
# 
# For example, "ACGAATTCCG" is a DNA sequence.
# 
# 
# When studying DNA, it is useful to identify repeated sequences within the
# DNA.
# 
# Given a string s that represents a DNA sequence, return all the
# 10-letter-long sequences (substrings) that occur more than once in a DNA
# molecule. You may return the answer in any order.
# 
# 
# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is either 'A', 'C', 'G', or 'T'.
# 
# 
#

# @lc code=start
class Solution:
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     length = len(s)
    #     laststring = ''
    #     res = []
    #     for start in range(0,length-10):
    #         end = start + 10
    #         substring = s[start:end]
    #         if substring == laststring:
    #             continue
    #         laststring = substring   
    #         if substring in res:
    #             continue
    #         if substring in s[start+1: ] :
    #             res.append(substring)

    #     return res
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        d = {}
        for start in range(0, length-9):
            end = start + 10
            substring = s[start:end]
            if substring in d:
                d[substring] += 1
            else:
                d[substring] = 1
        
        res = []
        for k,v in d.items():
            if v > 1:
                res.append(k)
        return res

# @lc code=end

