#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (51.39%)
# Likes:    4821
# Dislikes: 214
# Total Accepted:    480.7K
# Total Submissions: 935.3K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: root = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# 
# 
#
class TreeNode(object):
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        inOrder = self.inOrder(root)
        preOrder = self.preOrder(root)
        return '|'.join([inOrder, preOrder])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        inOrder, preOrder = data.split('|')
        return self.order2Node(inOrder, preOrder)

    def order2Node(self, inOrder, preOrder):
        assert len(inOrder) == len(preOrder), 'lenght error'
        if len(inOrder)==0:
            return None
            
        val = preOrder[0]
        root = TreeNode(val)
        index = inOrder.index(val)
        left_inorder = inOrder[ :index]
        right_inorder = inOrder[index+1: ]

        left_length = len(left_inorder)
        left_preorder = preOrder[1:left_length+1]
        right_preorder = preOrder[left_length+1: ]

        left = self.order2Node(left_inorder, left_preorder)
        right = self.order2Node(right_inorder, right_preorder)
        root.left = left
        root.right = right
        return root

    def inOrder(self, root):
        """ in order seq of root
        
        type root: TreeNode
        rtype: str
        """
        if root==None:
            return ''

        left = self.inOrder(root.left)
        right = self.inOrder(root.right)
        return str(root.val).join([left, right])

    def preOrder(self, root):
        """pre order seq of root
        
        """
        if root==None:
            return ''

        left = self.preOrder(root.left)
        right = self.preOrder(root.right)
        return str(root.val) + left + right


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

