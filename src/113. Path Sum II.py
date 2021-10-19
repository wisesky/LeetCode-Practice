from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        # if root == None:
        #     return res
        
        self.helper(root, sum, [], res)
        return res

    def helper(self, root,sum, r, res):
        if root == None:
            return 
        if root.left==None and root.right==None:
            if root.val == sum:
                # r.append(root.val)
                res.append(r+[root.val])
            return 
        
        self.helper(root.left, sum-root.val, r+[root.val], res)
        self.helper(root.right, sum-root.val, r+[root.val], res)
        return