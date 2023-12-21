#! python3
# -*- encoding: utf-8 -*-
'''
@File   : LIS.py
@Time   : 2023/08/15 19:29:00
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 

最长不下降子序列

给定一个长度为 n 的序列 A（n \leq 5000），求出一个最长的 A 的子序列，满足该子序列的后一个元素不小于前一个元素。

'''
"""设 f(i) 表示以 A_i 为结尾的最长不下降子序列的长度，则所求为 \max_{1 \leq i \leq n} f(i)。
计算 f(i) 时，尝试将 A_i 接到其他的最长不下降子序列后面，以更新答案。于是可以写出这样的状态转移方程：f(i)=\max_{1 \leq j < i, A_j \leq A_i} (f(j)+1)。

容易发现该算法的时间复杂度为 O(n^2)。
"""
class Solution:
    def longestIncreasingSequence(self, nums):
        l = len(nums)
        dp = [1 for _ in range(l+1)]
        seqTo = {}
        #dp[0] = 1
        for i, num in enumerate(nums):
            v = dp[i]
            for j in range(i):
                if nums[j] < num:
                    if v < dp[j] + 1:
                        seqTo[i] = j
                        v = dp[j] + 1
                    # v = max(v, dp[j] + 1)
                    
            dp[i] = v
        print(dp)
        print(seqTo)
        idx = dp.index(max(dp))
        res = []
        while idx != None:
            res.insert(0, nums[idx])
            idx = seqTo.get(idx)
        print(res)
        return 0
if __name__ == "__main__":
    dp = [4,5,6,3]
    #dp = [4,5,6,3,8]
    so = Solution()
    res = so.longestIncreasingSequence(dp)
    #print(res)

"""
当 n 的范围扩大到 n \leq 10^5 时，第一种做法就不够快了，下面给出了一个 O(n \log n) 的做法。

首先，定义 a_1 \dots a_n 为原始序列，d 为当前的不下降子序列，len 为子序列的长度，那么 d_{len} 就是长度为 len 的不下降子序列末尾元素。

初始化：d_1=a_1,len=1。

现在我们已知最长的不下降子序列长度为 1，那么我们让 i 从 2 到 n 循环，依次求出前 i 个元素的最长不下降子序列的长度，循环的时候我们只需要维护好 d 这个数组还有 len 就可以了。关键在于如何维护。

考虑进来一个元素 a_i：

元素大于等于 d_{len}，直接将该元素插入到 d 序列的末尾。
元素小于 d_{len}，找到 第一个 大于它的元素，用 a_i 替换它。
"""

dp = [0x1f1f1f1f] * MAXN
mx = dp[0]
for i in range(0, n):
    bisect.insort_left(dp, a[i], 0, len(dp))
ans = 0
while dp[ans] != mx:
    ans += 1
