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
        if n <= 2:
            return 0
        marked = set()
        count = 1
        marked.add(2)
        for i in range(3, n, 2):
            if self.isPrime(i, marked):
                count += 1
        # return len(marked)
        return count

    def isPrime(self, x, marked):
        if x == 0 or x == 1:
            return False
        sx = x**0.5
        ceil = math.ceil(sx)
        ceil = x if ceil >= x else ceil+1
        for i in range(3, ceil,2):
            if i in marked and x % i == 0:
                return False
        
        marked.add(x)
        return True
# @lc code=end

if __name__ == "__main__":
    n = 1500000
    # n = 5000000
    so = Solution()
    r = so.countPrimes(n)
    print(r)

