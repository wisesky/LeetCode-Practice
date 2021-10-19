# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None or q == None:
            return p == q
        
        r1 = self.isSameTree(p.left, q.left)
        r2 = self.isSameTree(p.right, q.right)
        return r1 and r2 and p.val == q.val
