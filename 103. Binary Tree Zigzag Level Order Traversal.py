from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = deque()
        self.order(root, 0,res)
        return list(res)

    def order(self, root, level, res):
        if root == None:
            return 

        while level >= len(res):
            res.append([])

        if level % 2 == 0:
            res[level].append(root.val)
            self.order(root.left, level+1, res)
            self.order(root.right, level+1, res)
        else:
            res[level].insert(0, root.val)
            self.order(root.left, level+1, res)
            self.order(root.right, level+1, res)

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


nums = [1,2,3,None, None, 4,5 ]
root = initTree(1, nums)

so = Solution()
res = so.zigzagLevelOrder(root)
print(res)