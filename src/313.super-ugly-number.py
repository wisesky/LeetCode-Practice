#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (46.92%)
# Likes:    1066
# Dislikes: 187
# Total Accepted:    93.8K
# Total Submissions: 198.8K
# Testcase Example:  '12\n[2,7,13,19]'
#
# A super ugly number is a positive integer whose prime factors are in the
# array primes.
# 
# Given an integer n and an array of integers primes, return the n^th super
# ugly number.
# 
# The n^th super ugly number is guaranteed to fit in a 32-bit signed
# integer.
# 
# 
# Example 1:
# 
# 
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
# super ugly numbers given primes = [2,7,13,19].
# 
# 
# Example 2:
# 
# 
# Input: n = 1, primes = [2,3,5]
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# in the array primes = [2,3,5].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^6
# 1 <= primes.length <= 100
# 2 <= primes[i] <= 1000
# primes[i] is guaranteed to be a prime number.
# All the values of primes are unique and sorted in ascending order.
# 
# 
#
from typing import List
# @lc code=start
from collections import deque
import heapq
from sortedcontainers import SortedSet
class Solution:
    """
    TLE: n=100000
    每次输出的结果 crt * [primes] 得到新的 待选数列， 添加到cdd中
    只不过每个crt 会产生 len(primes) 长度的待选数列，
    这样cdd就会 以 n*len(primes)的速率增加，很容易产生远远超过n的cdd
    最好的方式是，一次crt 产生一个 cdd 
    """
    # def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    #     crt = 1
    #     c = 1
    #     # cdd = deque(primes)
    #     cdd = primes.copy()
    #     # heapq.heapify(cdd)
    #     cdd = SortedSet(cdd)

    #     while c + len(cdd) < n:
    #         # crt = heapq.heappop(cdd)
    #         # _ = [heapq.heappush(cdd,x*crt) for x in primes if x*crt not in cdd]
    #         crt = cdd.pop()
    #         _ = [cdd.add(x*crt) for x in primes]
    #         c += 1
       
    #     return crt

    def nthSuperUglyNumber(self, n, primes):
        """
        上述方法自己无意间给自己加了一个限制，导致始终没办法找到可以一次crt产生一个cdd方法
        这个限制是要求自己不存储所有 结果，必须要stream 的方式输出结果，以为当n很大的时候，存储这些结果没必要
        然而 cdd 以 n*len(primes)的速率递增，显然占用了数倍于n的内存，得不偿失
        res     primes          cdd
        1   *   [2,7,13,19]   [2,7,13,19]
        2   *   [2,7,13,19]   [4,14,26,38]
        4   *   [2,7,13,19]   [8,28,52,76]
        7   *   [2,7,13,19]   [14,49,91, 133]
        8   *   [2,7,13,19]    ....

        要根据输出的 2(res) 将生成 [4,14,26,39](primes) 
        这里我就陷入了迷惑， 其实更深挖掘一下，发现 4(cdd) 是由 primes + 2(res) 组成的
        primes 已知，只需要保存2就可以了，之前stream的输出方式，无法取到2, 如果改用保存历史res的方式
        那么就可以通过索引index->2(res),通过res_index, primes_index -> 4
        这样做存在一个问题是，正确性无法得到保证，因为正确的seq， 4 之后 应该是 7，8，而不是14，如果只是把4 当作14的pre，那么必然存在错过8的问题
        
        观察上表会发现，primes 中的每一个 prime 构成一个链表，类似于多个链表合并排序思想
        只需要res_index, prime(表示所属链表) -> prime链表当前val
        同时可以得到 一个链表内，下一个值 res_index+1 -> res_next_val * prime  prime 链表下一个val

        总结，反思，没有宏观分析 sample, 试图在sample分析阶段偷懒，其实把上表的迭代过程 清晰的展现出来，
        就能发现自己添加的无必要的限制， 和正确的程序演绎逻辑，果然 Dijkstra大神强调 程序结构的正确性，且易推理是非常非常重要的
        试图 quick and dirty 的写代码， 有时候会得不偿失
        所以尽量保证思路清晰的情况下写代码， 遇到问题，更需要关注思路上结构上的正确性，不要在细节上斤斤计较，
        虽然有时候确实是自己的细节问题，导致程序出现bug，让自己本能的过分在意细节，但是bug毕竟还是可以修复
        思路走偏，再怎么debug也是于事无补的
        """
        # val, prime, index
        cdd  = [(x, x, 0) for x in primes]
        heapq.heapify(cdd)
        nums = [1]
        c = 1

        while c < n:
            val, prime, index = heapq.heappop(cdd)
            if val != nums[-1]:
                nums.append(val)
                c += 1

            heapq.heappush(cdd, (prime*nums[index+1], prime, index+1))

        return nums[-1]

        

# @lc code=end

so = Solution()

n = 12
primes = [2,7,13,19]
n = 1
primes = [2,3,5]
print(so.nthSuperUglyNumber(n, primes))
