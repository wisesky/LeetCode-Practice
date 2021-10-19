# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        r1 = self.postorderTraversal(root.left)
        r2 = self.postorderTraversal(root.right)
        return r1 + r2 +[root.val]