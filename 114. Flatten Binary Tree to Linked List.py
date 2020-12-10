# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        return
        

    def helper(self, root):
        if root == None:
            return None

        left = self.helper(root.left)        
        right = self.helper(root.right)

        pre = root
        cur = left
        while cur != None:
            pre = cur
            cur = cur.right
        
        root.left = None
        root.right = left
        pre.right = right
        return root
