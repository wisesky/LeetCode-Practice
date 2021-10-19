#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (41.37%)
# Likes:    1428
# Dislikes: 73
# Total Accepted:    104.7K
# Total Submissions: 242.2K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use preorder traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as '#'.
# 
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
# 
# Given a string of comma-separated values preorder, return true if it is a
# correct preorder traversal serialization of a binary tree.
# 
# It is guaranteed that each comma-separated value in the string must be either
# an integer or a character '#' representing null pointer.
# 
# You may assume that the input format is always valid.
# 
# 
# For example, it could never contain two consecutive commas, such as "1,,3".
# 
# 
# Note: You are not allowed to reconstruct the tree.
# 
# 
# Example 1:
# Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# Example 2:
# Input: preorder = "1,#"
# Output: false
# Example 3:
# Input: preorder = "9,#,#,1"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 10^4
# preorder consist of integers in the range [0, 100] and '#' separated by
# commas ','.
# 
# 
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        88ms(5%) 14.5MB(13%)
        树基本都是 DFS
        但是找不到合适的标示合法二叉树的变量，最后还是通过树的占用字符数来划分字符串
        划分过程出现的任何不合理情况就可以直接返回 False
        此外，一些边界情况也需要区分
        """
        preorder= preorder.split(',')
        if len(preorder)==0:
            return True
        if preorder[0] == '#' :
            if len(preorder)==1:
                return True
            else:
                return False
        left_length = self.treeLength(preorder[1: ])
        if left_length==0:
            return False
        right_length = self.treeLength(preorder[1+left_length: ])
        if right_length==0:
            return False
        tree_length = 1 + left_length + right_length
        return tree_length == len(preorder)
        
    def treeLength(self, preorder):
        """
        统计 当前preorder 下的二叉树占用字符数
        """
        if len(preorder) == 0:
            return 0
        if preorder[0]=='#':
            return 1
        left_length = self.treeLength(preorder[1: ])
        right_length = self.treeLength(preorder[1+left_length: ])
        return 1 + left_length + right_length
# @lc code=end

so = Solution()

preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
preorder = "1,#"
preorder = '9,#,#,1'
preorder = "#,#,#"
print(so.isValidSerialization(preorder))
