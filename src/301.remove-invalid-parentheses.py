#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (45.48%)
# Likes:    3757
# Dislikes: 178
# Total Accepted:    286.9K
# Total Submissions: 630.2K
# Testcase Example:  '"()())()"'
#
# Given a string s that contains parentheses and letters, remove the minimum
# number of invalid parentheses to make the input string valid.
# 
# Return all the possible results. You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "()())()"
# Output: ["(())()","()()()"]
# 
# 
# Example 2:
# 
# 
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# 
# 
# Example 3:
# 
# 
# Input: s = ")("
# Output: [""]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if s is None:
            return [""]
        self.result = set()
        self.maxLength = -1
        self.searchValidParentheses( "",s,  0)
        return list(self.result) if len(self.result) != 0 else [""]
    
    def searchValidParentheses(self, chosen, reserved,balance):
        # invalid 状态，多一个）
        if balance < 0 :
            return
        # 终止状态，待选字符为0
        if len(reserved) == 0:
            # valid状态
            if balance == 0 :
                # 筛选最长有效字符
                if len(chosen) < self.maxLength:
                    return
                # 遇到更长字符，重置result
                if len(chosen) > self.maxLength:
                    self.result = set()
                    self.maxLength = len(chosen)
                # 更新 result
                self.result.add(chosen)
            return
        if reserved[0] == '(':
            val = 1 
        elif reserved[0] == ')':
            val = -1
        else: # 非() 字符，直接添加
            # 带上字符，不影响balance
            self.searchValidParentheses(chosen+reserved[0], reserved[1: ], balance)
            return
        # 带上字符， 影响balance
        self.searchValidParentheses(chosen+reserved[0], reserved[1: ], balance+val)
        # 不带上字符， 不影响balance
        self.searchValidParentheses(chosen,reserved[1: ], balance )      
        return       
                
# @lc code=end

if __name__=="__main__":
    so = Solution()
    s = '()())()'
    s = "(a)())()"
    s = ")("
    result = so.removeInvalidParentheses(s)
    print(result)
