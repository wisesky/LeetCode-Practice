#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Medium (45.51%)
# Likes:    1053
# Dislikes: 1132
# Total Accepted:    225.8K
# Total Submissions: 496K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the Bulls and Cows game with your friend.
# 
# You write down a secret number and ask your friend to guess what the number
# is. When your friend makes a guess, you provide a hint with the following
# info:
# 
# 
# The number of "bulls", which are digits in the guess that are in the correct
# position.
# The number of "cows", which are digits in the guess that are in your secret
# number but are located in the wrong position. Specifically, the non-bull
# digits in the guess that could be rearranged such that they become bulls.
# 
# 
# Given the secret number secret and your friend's guess guess, return the hint
# for your friend's guess.
# 
# The hint should be formatted as "xAyB", where x is the number of bulls and y
# is the number of cows. Note that both secret and guess may contain duplicate
# digits.
# 
# 
# Example 1:
# 
# 
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
# ⁠ |
# "7810"
# 
# Example 2:
# 
# 
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
# ⁠ |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the
# non-bull digits can only be rearranged to allow one 1 to be a bull.
# 
# 
# Example 3:
# 
# 
# Input: secret = "1", guess = "0"
# Output: "0A0B"
# 
# 
# Example 4:
# 
# 
# Input: secret = "1", guess = "1"
# Output: "1A0B"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= secret.length, guess.length <= 1000
# secret.length == guess.length
# secret and guess consist of digits only.
# 
# 
#

# @lc code=start
class Solution:
    """
    
    """
    def getHint(self, secret: str, guess: str) -> str:
        numBalance = {}

        count_a = 0
        count_b = 0
        for m,n in zip(secret, guess):
            if m==n:
                count_a += 1
                continue
            if m in numBalance:
                numBalance[m] += 1
                if numBalance[m] <= 0:
                    count_b += 1
            else:
                numBalance[m] = 1

            if n in numBalance:
                numBalance[n] -= 1
                if numBalance[n] >= 0:
                    count_b += 1
            else:
                numBalance[n] = -1

        # count_b = 0
        # for num, bls in numBalance.items():
        #     if bls == 0:
        #         count_b += 1

        return str(count_a) + 'A' + str(count_b) + 'B'

# @lc code=end

so = Solution()
print(so.getHint('1123', '0111'))
print(so.getHint('1807', '7810'))
print(so.getHint('1', '0'))
print(so.getHint('1', '1'))
print(so.getHint('1122','2211'))