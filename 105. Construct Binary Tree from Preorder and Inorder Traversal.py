from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        val = preorder[0] 
        pos = inorder.index(val)

        node = TreeNode(val)
        node.left = self.buildTree(preorder[1:pos+1], inorder[ :pos])
        node.right = self.buildTree(preorder[pos+1: ], inorder[pos+1: ])
        return node