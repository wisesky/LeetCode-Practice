#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (57.04%)
# Likes:    4167
# Dislikes: 227
# Total Accepted:    466.1K
# Total Submissions: 817.1K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root = [1,null,3]
# Output: [1,3]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        r = []
        self.rightSide(root, 1,r)
        return r
        
    def rightSide(self, root, level,r):
        if root == None:
            return
        if len(r) < level:
            r.append(root.val)
        else:
            r[level-1] = root.val
        
        self.rightSide(root.left, level+1,r)
        self.rightSide(root.right, level+1,r)
        return


# @lc code=end

