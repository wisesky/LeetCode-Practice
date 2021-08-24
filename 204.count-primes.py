#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (32.80%)
# Likes:    3356
# Dislikes: 820
# Total Accepted:    502K
# Total Submissions: 1.5M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# 
# Example 1:
# 
# 
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
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
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 5 * 10^6
# 
# 
#

# @lc code=start
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        marked = [1] * n
        marked[0] = 0
        marked[1] = 0
        # marked[2] = 1
        for i in range(2, n):
            if marked[i] == 1:
                c = 2
                while c*i < n:
                    marked[c*i] = 0
                    c += 1
        return sum(marked) 

# @lc code=end

if __name__ == "__main__":
    n = 1500000
    # n = 5000000
    n = 10
    so = Solution()
    r = so.countPrimes(n)
    print(r)

