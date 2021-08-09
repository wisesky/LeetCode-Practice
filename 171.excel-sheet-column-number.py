#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r = 0
        for i, char in enumerate(reversed(columnTitle)):
            c = ord(char) - ord('A') + 1
            r += c * (26**i)
        return r

# columnTitle = 'FXSHRXW'
# so = Solution()
# r = so.titleToNumber(columnTitle)
# print(r)

# @lc code=end

