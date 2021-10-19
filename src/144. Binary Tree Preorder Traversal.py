# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # s1 dfs
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        r = []
        self.preOrder(root,r)
        return r

    def preOrder(self, root, r):
        if root == None:
            return
        r.append(root.val)
        self.preOrder(root.left,r)
        self.preOrder(root.right,r)    
        return
    # s2 dfs
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        r1 = self.preorderTraversal(root.left)
        r2 = self.preorderTraversal(root.right)
        return [root.val] + r1 + r2
