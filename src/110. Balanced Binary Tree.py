# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # if root == None:
            # return True
        r, _ = self.height(root)
        return r

    def height(self, root):
        if root == None:
            return True, 0

        r1, h1 = self.height(root.left)
        r2, h2 = self.height(root.right)
        return r1 and r2 and abs(h1-h2) <= 1 , max(h1, h2) + 1