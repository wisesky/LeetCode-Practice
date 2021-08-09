#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (28.66%)
# Likes:    1623
# Dislikes: 3983
# Total Accepted:    251.9K
# Total Submissions: 876K
# Testcase Example:  '123'
#
# Convert a non-negative integer num to its English words representation.
# 
# 
# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# Example 4:
# Input: num = 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
# Constraints:
# 
# 
# 0 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    """
    总体思路是，按英文数字表示习惯，每3位，变换一次表示后缀，Billion,Million,Thousand
    3位以内，可以共用一个规则表示，用 lower 函数来单独处理
    本题是Hard的主要原因是 英文数字表达的细节容易出错，
    此外 1,000,000 - > one million， 程序容易输出 one million thousand 
    这就需要在每隔3位 添加 billion million 的时候，判断 高位部分时候如果为空， 则不添加多余的 thousand
    """
    def __init__(self) -> None:
        """
        初始化不同位数的数字英文单词映射关系
        """
        self.c2s = {
            # 0: '' ,
            1: 'Thousand',
            2: 'Million',
            3: 'Billion',
        }
        self.n2s = {
            1:'One',
            2:'Two',
            3: 'Three',
            4:'Four',
            5:'Five',
            6:'Six',
            7:'Seven',
            8:'Eight',
            9:'Nine',
        }
        self.t2s = {
            10:'Ten',
            11:'Eleven',
            12:'Twelve',
            13:'Thirteen',
            14:'Fourteen',
            15:'Fifteen',
            16:'Sixteen',
            17:'Seventeen',
            18:'Eighteen',
            19:'Nineteen',
        }
        self.o2s = {
            2:'Twenty',
            3:'Thirty',
            4:'Forty',
            5:'Fifty',
            6:'Sixty',
            7:'Seventy',
            8:'Eighty',
            9:'Ninety',
        }

    def numberToWords(self, num: int) -> str:
        """
        每隔3位，分区而治， 
        1，3位以内转换英文，
        2，3位之间添加后缀

        最后把结果合并即可
        """
        if num == 0:
            return 'Zero'
        count = 0
        r = deque()
        while num != 0:
            # r.appendleft(self.c2s.get(count))
            lo = num%1000
            lower = self.lower(lo)
            if len(lower)!=0:
                # 如果高位部分为空，则不添加重复的3位表示的后缀，如 1,000,000 中多余的 thousand
                if count in self.c2s:
                    r.appendleft(self.c2s[count])
                r.appendleft(lower)
            count += 1
            num = num // 1000
        
        return ' '.join(r)

    def lower(self, num):
        """
        3位以内的数字 -> 英文 转换
        """
        hi, lo = num//100, num%100
        r = deque()
        if lo in self.t2s:
            r.appendleft(self.t2s[lo])
        else:
            o, n = lo//10, lo%10
            if n!=0:
                r.appendleft(self.n2s[n])
            if o in self.o2s:
                r.appendleft(self.o2s[o])
        if hi != 0:
            r.appendleft('Hundred')
            r.appendleft(self.n2s[hi])
        return ' '.join(r)
# @lc code=end

so = Solution()
num = 12345
# num = 1000000
num = 1234567891
print(so.numberToWords(num))
