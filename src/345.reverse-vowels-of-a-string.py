#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (46.07%)
# Likes:    1271
# Dislikes: 1640
# Total Accepted:    311K
# Total Submissions: 673.3K
# Testcase Example:  '"hello"'
#
# Given a string s, reverse only all the vowels in the string and return it.
# 
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
# cases.
# 
# 
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    # 68ms(49%) 15.1MB(49%)
    def reverseVowels(self, s: str) -> str:
        lo, hi = 0, len(s)-1
        s_org = list(s)
        vow1 = ['a','e','i','o','u']
        vow2 = [x.upper() for x in vow1]
        vows = set(vow1+vow2)


        while (lo < len(s)) and (s[lo] not in vows) :
            lo += 1

        while (hi >= 0) and (s[hi] not in vows):
            hi -= 1

        while lo < hi:
            tmp = s_org[lo]
            s_org[lo] = s_org[hi]
            s_org[hi] = tmp

            lo += 1
            hi -= 1
            while (lo < len(s)) and (s[lo] not in vows) :
                lo += 1
            while (hi >= 0) and (s[hi] not in vows):
                hi -= 1
            
        return ''.join(s_org)
# @lc code=end
so = Solution()

print(so.reverseVowels('aA'))
