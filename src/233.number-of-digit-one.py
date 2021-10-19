#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (32.07%)
# Likes:    432
# Dislikes: 782
# Total Accepted:    54.4K
# Total Submissions: 169.8K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
# 
# 
# Example 1:
# 
# 
# Input: n = 13
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: n = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        """"
        总体思想就是分类，先求所有数中个位是 1 的个数，再求十位是 1 的个数，再求百位是 1 的个数...

        假设 n = xyzdabc，此时我们求千位是 1 的个数，也就是 d 所在的位置。

        那么此时有三种情况，

        d == 0，那么千位上 1 的个数就是 xyz * 1000
                (0~xyz-1) 1 (0~abc)
                [0,xyz-1] : length: xyz
                [0,abc]: length: 1000
                so: xyz*1000
        d == 1，那么千位上 1 的个数就是 xyz * 1000 + abc + 1
                d==1 包含 d==0且还有需要考虑的情况
                (xyz) 1 (0~abc)
                [0,abc]: length: abc+1
        d > 1，那么千位上 1 的个数就是 xyz * 1000 + 1000
                d>1 包含 d==1 
                (xyz)1(0~999)
                [0,999]: 1000
        """
        str_n = str(n)
        length = len(str_n)
        
        count = 0
        for i in range(length):
            base = 10**(length-i-1)
            right = str_n[i+1: ]
            left = str_n[ :i]
            mid = int(str_n[i])
            right = 0 if len(right)==0 else int(right)
            left = 0 if len(left)==0 else int(left)
            
            count1 = left*base
            count2 = right+1
            count3 = base

            if mid == 0:
                # return count1
                count += count1
            elif mid == 1:
                # return count1+count2
                count += count1 + count2
            else:
                # return count1+count3
                count += count1 + count3
        return count
# @lc code=end
if __name__ == '__main__':
    so = Solution()
    n = 13
    n = 0
    r = so.countDigitOne(n)
    print(r)
