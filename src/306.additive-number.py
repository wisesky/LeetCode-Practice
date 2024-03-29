#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#
# https://leetcode.com/problems/additive-number/description/
#
# algorithms
# Medium (29.90%)
# Likes:    606
# Dislikes: 560
# Total Accepted:    63.1K
# Total Submissions: 210.1K
# Testcase Example:  '"112358"'
#
# Additive number is a string whose digits can form additive sequence.
# 
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the sum
# of the preceding two.
# 
# Given a string containing only digits '0'-'9', write a function to determine
# if it's an additive number.
# 
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence
# 1, 2, 03 or 1, 02, 3 is invalid.
# 
# 
# Example 1:
# 
# 
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5,
# 8. 
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# Example 2:
# 
# 
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199
# 
# 
# 
# Constraints:
# 
# 
# num consists only of digits '0'-'9'.
# 1 <= num.length <= 35
# 
# 
# Follow up:
# How would you handle overflow for very large input integers?
# 
#

# @lc code=start
class Solution:
    """
    32ms(59%) 14MB(95%)
    由于first 2 nums 长度未定，所以就要遍历所有可能的长度
    长度确定的情况下，就可以递归的验证Additive Seq 是否成立
    注意03,02 这种非法字符，要自己去验证
    """
    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)
        for a_length in range(1,length//2+1):
            for b_length in range(1,length-a_length):
                if self.isValid(num, a_length, b_length):
                    return True
        else:
            return False

    def isValid(self, num, a_length, b_length):
        a = num[ :a_length]
        b = num[a_length:a_length+b_length]
        if self.notValidChar(a) or self.notValidChar(b):
            return False
        a_num, b_num = int(a), int(b)
        c_num = a_num + b_num
        c = str(c_num)
        c_length = len(c)
        c_start = a_length + b_length
        c_end = c_start + c_length
        c_origin = num[c_start:c_end]
        if c_origin != c:
            return False
        if c_end >= len(num):
            return True

        return self.isValid(num[a_length: ], b_length, c_length)
    
    def notValidChar(self, char):
        if char == '0':
            return False
        return char.startswith('0')
    # 另一个时候做题，想起了完全一样的解题思路的代码
    def isAdditiveNumber(self, num: str) -> bool:
        self.flag = False
        for i in range(1,len(num)):
            for j in range(i+1, len(num)):
                # 排除 p1 == ‘0x'的情况
                if num[0] == '0' and i >1 :
                    continue
                # 排除 p2 == '0x' 的情况
                if num[i]=='0'and j-i>1:
                    continue
                p1 = int(num[ :i])
                p2 = int(num[i:j])
                self.cut(p1, p2, num[j: ])
                if self.flag :
                    return True
        return False
        # pre1 + pre2 == num[ :x]
    def cut(self, p1, p2, reserved):
        # print(f'now p1: {p1}, p2:{p2}')
        if len(reserved) == 0:
            self.flag = True
            # print(f'last p1: {p1}, p2:{p2}')
            return
        p_str = str(p1 + p2)
        # zip 函数自动挑选最短的，如果 reserved 太短，则说明不匹配
        if len(p_str) > len(reserved):
            return
        # 匹配对应字符
        for l, r in zip(p_str, reserved):
            if l != r:
                return
        new_p1 = p2
        new_p2 = int(reserved[ :len(p_str)])
        self.cut(new_p1,new_p2, reserved[len(p_str): ])
        return
# @lc code=end

# @lc code=end

so = Solution()
num = '112358'
num = '199100199'
num = '123'
num = '1023'
num = '101'
# print(so.isValid(num, 1, 1))
print(so.isAdditiveNumber(num))