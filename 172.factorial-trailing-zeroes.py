#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
# 原题是求阶乘之后末尾的0的个数
# 最简洁的方案是采用数学技巧： 因式分解之后 10 的个数
# 10 = 2 * 5
# 考虑到阶乘中，2 出现的次数远远多余5，所以只需要计算 5 出现的次数即可
# 阶乘中， 1 2 3 4 5 ｜6 7 8 9 2*5 ｜ 11 12 13 14 3*5
# 每隔 5 位，出现 一次 5 ： 共有 n // 5  个 5
# 1..25 |25.. 2*25| 51 .. 3*25
# 每隔 25 位，出现 两次 5 : 共有 n // 25 个 25
# 注意，上述累加起来就是，所有5的个数， 因为 25 = 5 * 5 ，
# 第一轮计算5出现次数时候，计算了一次5， 第二次 算25 的时候，再累加上去，
# 所以25 出现两次5的时候，实际上只需要重复累加一次25 中的一次5即可
# 以此类推:  n // 5 + n // 25  + n //125 + ..
# 即是n！ 末尾的 0 的个数
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n==0 else n//5 + self.trailingZeroes(n//5)
# @lc code=end
if __name__=='__main__':
    so = Solution()
    n = 7
    r = so.trailingZeroes(n)
    print(r)