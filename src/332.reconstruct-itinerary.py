#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (38.71%)
# Likes:    3161
# Dislikes: 1406
# Total Accepted:    236.3K
# Total Submissions: 604.2K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# You are given a list of airline tickets where tickets[i] = [fromi, toi]
# represent the departure and the arrival airports of one flight. Reconstruct
# the itinerary in order and return it.
# 
# All of the tickets belong to a man who departs from "JFK", thus, the
# itinerary must begin with "JFK". If there are multiple valid itineraries, you
# should return the itinerary that has the smallest lexical order when read as
# a single string.
# 
# 
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
# ["JFK", "LGB"].
# 
# 
# You may assume all tickets form at least one valid itinerary. You must use
# all the tickets once and only once.
# 
# 
# Example 1:
# 
# 
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# 
# 
# Example 2:
# 
# 
# Input: tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi
# 
# 
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        144ms(11%) 14,7MB(74%)
        """
        adjs = {}
        # reversed_adjs = {}
        for start,end in tickets:
            if start in adjs:
                adjs[start].append(end)
            else:
                adjs[start] = [end]

        for start in adjs:
            adjs[start].sort(reverse=True)

        res = self.dfs('JFK', adjs, len(tickets))
        return  res

    def dfs(self, start, adjs, left):
        """
        start： DFS 起点
        left： 还剩下 多少步 结束搜索
        """
        jumps = adjs.get(start, [])
        if left==0:
            return [start]
        if len(jumps) == 0:
            return []
        
        for index in range(len(jumps)):
            pos = len(jumps) - index - 1
            j = jumps.pop(pos)
            r = self.dfs(j, adjs, left-1)
            if len(r) == left:
                return [start] + r
            jumps.insert(pos, j)
        return []


# @lc code=end

so = Solution()

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# tickets = [['JFK', 'TEST'], ['TEST', 'JFK']]

print(so.findItinerary(tickets))