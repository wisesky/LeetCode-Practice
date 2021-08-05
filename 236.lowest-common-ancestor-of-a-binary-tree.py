#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (50.99%)
# Likes:    6533
# Dislikes: 219
# Total Accepted:    711.7K
# Total Submissions: 1.4M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        inOrderVal = self.inOrder(root)
        val2ids = {}
        for ids, val in enumerate(inOrderVal):
            val2ids[val] = ids 
        return self.dfsSearch(root, p, q, val2ids)
        
    def inOrder(self, root):
        if root==None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)        

    def dfsSearch(self, root, p, q, val2ids):
        if root == None:
            return None
        rootIds = val2ids[root.val]    
        pIds = val2ids[p.val]
        qIds = val2ids[q.val]
        if pIds <= rootIds and qIds >= rootIds:
            return root
        if pIds >= rootIds and qIds <= rootIds:
            return root
        if pIds < rootIds and qIds < rootIds:
            return self.dfsSearch(root.left, p, q, val2ids)
        if pIds > rootIds and qIds > rootIds:
            return self.dfsSearch(root.right, p, q, val2ids)
# @lc code=end

