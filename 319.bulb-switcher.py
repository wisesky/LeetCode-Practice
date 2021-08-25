#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#
# https://leetcode.com/problems/bulb-switcher/description/
#
# algorithms
# Medium (45.82%)
# Likes:    722
# Dislikes: 1353
# Total Accepted:    98.8K
# Total Submissions: 214.5K
# Testcase Example:  '3'
#
# There are n bulbs that are initially off. You first turn on all the bulbs,
# then you turn off every second bulb.
# 
# On the third round, you toggle every third bulb (turning on if it's off or
# turning off if it's on). For the i^th round, you toggle every i bulb. For the
# n^th round, you only toggle the last bulb.
# 
# Return the number of bulbs that are on after n rounds.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 1
# Explanation: At first, the three bulbs are [off, off, off].
# After the first round, the three bulbs are [on, on, on].
# After the second round, the three bulbs are [on, off, on].
# After the third round, the three bulbs are [on, off, off]. 
# So you should return 1 because there is only one bulb is on.
# 
# Example 2:
# 
# 
# Input: n = 0
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: n = 1
# Output: 1
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
    # def bulbSwitch(self, n: int) -> int:
    #     """
    #     TLE:     n=9999999 O(n**2)
    #     """ 
    #     li = [1 for _ in range(n)]
    #     for ith in range(1,n):
    #         self.toggle(li, ith, n)
    #     return sum(li)

    # def toggle(self, li, ith, n):
    #     """
    #     switch bulb in ith round
    #     """
    #     for i in range(ith,n,ith+1):
    #         self.switch(li, i)
        
    # def switch(self, li, i):
    #     """
    #     switch li[i]
    #     """
    #     if li[i] == 0:
    #         li[i] = 1
    #     else:
    #         li[i] = 0

    # def bulbSwitch(self, n):
    #     """
    #     TLE: n=99999 O(n**2)
    #     """
    #     # res = 0
    #     res = []
    #     for ith in range(1, n+1):
    #         r = self.isOn(ith)
    #         # res += r
    #         res.append(r)
    #     return res

    def isOn(self, ith):
        """
        得到 第 ith 个位置上的灯， 被重复toggle的次数
        """
        r = 0
        for i  in range(2,ith+1):
            if ith % i == 0:
                r += 1
        # return 1 if r % 2 == 0 else 0
        return (r+1) % 2

    def bulbSwitch(self, n):
        """
        40ms(10%) 14.2MB(63%)
        数学归纳发现：只有 i**2 的灯是亮的 
        eg: 1, 4, 9, 16, 25 ...

        更进一步观察： 非平方根的数, 其 isOn 的结果永远是奇数
        eg:
        5: 5            1
        6: 6 3 2        3
        7: 7            1
        8: 8 4 2        3
        10: 10 5 2      3
        11: 11          1
        12: 12 6 4 3 2  5
        ...

        结论， 质数 isOn 个数一定是 1 
            由多个不同的质数混合而成的情况
            a b a*b -> 3
            a b c ab ac bc abc -> 7

            假设是由m个不同个质数 组成的，那么 isOn 数目就是
            C^(1)_(m) + C^(2)_(m) + C^(3)_(m) + ...
            + C^(m)_(m)
            = 2**m - 1
            必然是奇数

            只有平方数，会包含自身以及其平方根 构成偶数
            9 : 9,3
            16: 16, 4
            81: 81, 9
        """
        r = 0
        s = 1
        while s**2 <= n:
            r += 1
            s += 1
        return r 

    def bulbSwitch(self, n):
        """
        Optim: 可根据n的平方根  直接取得结果
        32ms(48%) 14.1MB(63%)
        """
        return int(n**0.5)
# @lc code=end

so = Solution()

n = 99999
# n=3
# n=0
# n=1
print(so.bulbSwitch(n))
# res = so.bulbSwitch(n)
# for i in range(n):
#     if res[i] == 1:
#         print(i+1)