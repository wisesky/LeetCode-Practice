# from typing import bool
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        r1 = self.helper(root, False)
        r2 = self.helper(root, True)
        return max(r1, r2)
        

    # 划分包含root 和不包含root 无法递归所有情况， 因为此题主要是关键是是否可以继续扩展path
    # def helper(self, root, hasRoot : bool):
    #     if root == None:
    #         return float('-inf')

    #     if hasRoot:
    #         r1 =self.helper(root.left, hasRoot=True)
    #         r2 = self.helper(root.right, hasRoot=True)
    #         return max(root.val, root.val+r1, root.val+r2, root.val+r1+r2)
    #     else:
    #         r10 = self.helper(root.left, hasRoot=False)
    #         r11 = self.helper(root.left, hasRoot=True)
    #         r20 = self.helper(root.right, hasRoot=False)
    #         r21 = self.helper(root.right, hasRoot=True)
    #         return max(r10, r11, r20, r21)

    # 划分可扩展的path 和 不可扩展的path
    def helper(self, root, extend: bool):
        if root == None:
            return float('-inf')

        # 可扩展的情况，一定包含root,但是不能同时包含left right
        if extend:
            r1 = self.helper(root.left, extend=True)
            r2 = self.helper(root.right, extend=True)
            return max(root.val, root.val+r1, root.val+r2)
        # 不可扩展的情况，不包含root 和 同时包含root以及left and right
        else:
            r10 = self.helper(root.left, extend=False)
            r11 = self.helper(root.left, extend=True)
            r20 = self.helper(root.right, extend=False)
            r21 = self.helper(root.right, extend=True)
            return max(r10, r11, r20, r21, root.val+r11+r21)

    # 上述 self.helper(root, False) self.helper(root, True)会重复递归计算，现在合并减少重复递归
    def helper(self, root):
        if root == None:
            return float('-inf'), float('-inf')

        r10,r11 = self.helper(root.left)
        r20,r21 = self.helper(root.right)

        res1 = max(r10, r11, r20, r21, root.val+r11+r21)
        res2 = max(root.val, root.val+r11, root.val+r21)
        return res1, res2

