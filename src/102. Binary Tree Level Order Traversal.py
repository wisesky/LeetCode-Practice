from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.order(root, 0, res)
        return res

    def order(self, head, level, res):
        if head == None:
            return
        
        while level >= len(res):
            res.append([])

        res[level].append(head.val)

        self.order(head.left, level+1, res)
        self.order(head.right, level+1, res)
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

nums = [1,2,3,4,5,6,7]
root = initTree(1, nums)

so = Solution()
res = so.levelOrder(root)
print(res)