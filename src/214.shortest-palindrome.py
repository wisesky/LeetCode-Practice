#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (30.96%)
# Likes:    1756
# Dislikes: 156
# Total Accepted:    118.6K
# Total Submissions: 382.7K
# Testcase Example:  '"aacecaaa"'
#
# You are given a string s. You can convert s to a palindrome by adding
# characters in front of it.
# 
# Return the shortest palindrome you can find by performing this
# transformation.
# 
# 
# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of lowercase English letters only.
# 
# 
#

# @lc code=start
class Solution:
    """
    996 ms(6%) 14.7 MB(60%)
    shortest palindrome 的关键是 找到以 s[0] 为左边界
    的回文字符串的最长中心点 centor 

    扩展后的字符串 news 的中心点位置 i 恰好 等于回文字符串的长度-1
    """
    def shortestPalindrome(self, s: str) -> str:
        news = '_'.join(s)     
        long = 0
        for i in range(len(news)):
            pre = news[ :i]
            post = news[i+1:2*i+1][::-1]
            if pre == post:
                long = i
        rest = s[long+1: ][::-1]
        return rest + s



# @lc code=end

so = Solution()

s = 'aacecaaa'
s = 'abcd'
print(so.shortestPalindrome(s))