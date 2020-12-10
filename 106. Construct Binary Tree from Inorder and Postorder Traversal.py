from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        val = postorder[-1]
        pos = inorder.index(val)

        node = TreeNode(val)
        node.left = self.buildTree(inorder[ :pos], postorder[ :pos])
        node.right = self.buildTree(inorder[pos+1: ], postorder[pos:-1])
        return node