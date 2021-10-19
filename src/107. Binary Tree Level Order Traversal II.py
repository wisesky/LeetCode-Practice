from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, root, level,res):
        if root == None:
            return

        while level >= len(res):
            res.insert(0,[])

        res[-level-1].append(root.val)
        self.helper(root.left, level+1, res)
        self.helper(root.right, level+1, res)
        return

def initTree(pos, nums):
    if pos > len(nums):
        return None
    if nums[pos-1] == None:
        return None
    
    root = TreeNode(nums[pos-1])
    root.left = initTree(2*pos, nums)
    root.right = initTree(2*pos+1, nums)
    return root

nums = [3, 9, 20, None, None, 15, 7]
root = initTree(1, nums)

so = Solution()
res = so.levelOrderBottom(root)
print(res)
