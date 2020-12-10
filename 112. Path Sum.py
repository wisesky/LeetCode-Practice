# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        return self.helper(root, sum)

    def helper(self,root, sum):
        if root == None:
            return sum == 0
        if root.left == None:
            return self.helper(root.right, sum-root.val)
        if root.right == None:
            return self.helper(root.left, sum-root.val)

        b1 = self.helper(root.left, sum-root.val)
        b2 = self.helper(root.right,sum-root.val)
        return b1 or b2
