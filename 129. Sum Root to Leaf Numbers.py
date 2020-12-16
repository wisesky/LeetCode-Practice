# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        s= self.helper(root)
        su = [int(x) for x in s]
        return sum(su)

    def helper(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]

        s1 = self.helper(root.left)
        s2 = self.helper(root.right)
        s11 = [str(root.val)+x for x in s1]
        s22 = [str(root.val)+y for y in s2]
        return s11+s22