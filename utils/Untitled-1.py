""" 题目描述

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和≥ s的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        pre = []
        su = []
        for i,num in enumerate(nums):
            if num >= s:
                return 1
            if i == 0 or  pre[i-1] == -1:
                pre.append(-1)
                su.append(num)
                continue
            newsu = su[i-1] + num
            if newsu >= s:
                for j in range(pre[-1], i):
                    resu = newsu - nums[j]
                    if resu >= s:
                        newsu = resu
                    else:
                        break
                pre.append(j)
                su.append(newsu)
        mn = [float('inf')]
        for x, y in enumerate(pre):
            if y == -1:
                continue
            mn = min(mn, y-x+1)
        return mn
if __name__ == "__main__":
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    so = Solution.minSubArrayLen(s, nums)
    print(so)
