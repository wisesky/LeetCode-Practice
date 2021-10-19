# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res= []
        self.inOrder(root, res)
        if len(res) == 0:
            return True
        pre = res[0]
        for i in range(1,len(res)):
            if res[i] <= pre:
                return False
            pre = res[i]
        else:
            return True

    def inOrder(self, root, res):
        if root == None:
            return
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
        return

    # 思考如何直接用DFS ，而不是通过中序遍历来间接求解