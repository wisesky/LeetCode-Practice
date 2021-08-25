#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (35.31%)
# Likes:    3596
# Dislikes: 143
# Total Accepted:    146.4K
# Total Submissions: 411.6K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# A tree is an undirected graph in which any two vertices are connected by
# exactly one path. In other words, any connected graph without simple cycles
# is a tree.
# 
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
# where edges[i] = [ai, bi] indicates that there is an undirected edge between
# the two nodes ai and bi in the tree, you can choose any node of the tree as
# the root. When you select a node x as the root, the result tree has height h.
# Among all possible rooted trees, those with minimum height (i.e. min(h))  are
# called minimum height trees (MHTs).
# 
# Return a list of all MHTs' root labels. You can return the answer in any
# order.
# 
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.
# 
# 
# Example 1:
# 
# 
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node
# with label 1 which is the only MHT.
# 
# 
# Example 2:
# 
# 
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
# 
# 
# Example 3:
# 
# 
# Input: n = 1, edges = []
# Output: [0]
# 
# 
# Example 4:
# 
# 
# Input: n = 2, edges = [[0,1]]
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2 * 10^4
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated
# edges.
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    """
    marked: n=1717: TLE 
    father,a -> heigth n=2020: TLE
    memo: 372ms(15%) 23.5MB(5%)

    按照常规思路，用DFS，所以先把 edge 转化为邻接边 a2b
    随后用DFS遍历计算高度， 最初用 marked 标记已经遍历的vector
    随后发现树遍历，只需要搜索的时候，不要重复遍历父节点即可,
    即 (father, a) 唯一确定一个子树的长度， 由于常规的树结构一般都是类似于有向图
    所以无需刻意的mark 父节点， 但是这里是无向图，且确定用邻接边的存储方式，那么就需要排除父节点，避免循环遍历

    最后发现，在不同的root下，可能会重复便利相同的(father, a)，备忘录的方式optim :AC
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        a2b = {}
        for a,b in edges:
            if a in a2b:
                a2b[a].append(b)
            else:
                a2b[a] = [b]
            if b in a2b:
                a2b[b].append(a)
            else:
                a2b[b] = [a]

        # memo: father, a -> heigth
        memo = {}
        minHeight = float('inf')
        res = []
        for a in a2b:
            height = self.height(None,a,a2b,memo)
            if height < minHeight:
                res = [a]
                minHeight = height
            elif height == minHeight:
                res.append(a)
        return res

        
    def height(self, fat, a, a2b,memo):
        if (fat, a) in memo:
            return memo[fat, a]
        height = 0
        # marked[root] = True
        for b in a2b.get(a, []):
            # if not marked.get(b, False):
            if b == fat:
                continue
            height = max(height, self.height(a,b,a2b,memo))
        # marked[root] = False
        memo[fat,a] = height+1
        return height+1
# @lc code=end

so = Solution()

n = 4
edges = [
    [1,0],
    [1,2],
    [1,3]
]
# n = 2
# edges = [[0,1]]
print(so.findMinHeightTrees(n,edges))