""" 题目描述

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和≥ s的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        pre = 0
        su = 0
        le = 0
        for i,num in enumerate(nums):
            # print(su)
            if num >= s:
                return 1
            su += num
            if i == 0 or su < s:
                continue

            for j in range(pre, i):
                resu = su - nums[j]
                if resu >= s:
                    su = resu
                else:
                    break
            pre = j
            le = i - pre + 1 if le == 0 else min(i-pre+1, le)
        return le
if __name__ == "__main__":
    s = 7
    nums = [2, 3, 1, 2, 4, 3, 7]
    nums = [1,1]
    so = Solution()
    # so.minSubArrayLen(s, nums)
    print(so.minSubArrayLen(s, nums))
