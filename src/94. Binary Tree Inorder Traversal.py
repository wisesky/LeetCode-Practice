from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root == None:
            return 
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

def initTree(pos, nums):
    if pos > len(nums):
        return None
    if nums[pos-1] == None:
        return None
    
    root = TreeNode(nums[pos-1])
    root.left = initTree(2*pos, nums)
    root.right = initTree(2*pos+1, nums)
    return root

def inOrderPrint(root):
    if root == None:
        return
    inOrderPrint(root.left)
    print(root.val)
    inOrderPrint(root.right)
    return

nums = [1, None, 2, None, None,3]
so = Solution()
root = initTree(1,nums)
# inOrderPrint(root)

res = so.inorderTraversal(root)
print(res)

