# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        r = []
        self.inOrder(root, r)
        res = self.searchOuter(r)

        if len(res) < 1:
            return
        if len(res) == 1:
            val1, val2 = res[0]
        else:
            val1, val2 = res[0][0], res[1][1]
            
        node1 = self.searchNode(root, val1)
        node2 = self.searchNode(root, val2)
        if node1 == None or node2 == None:
            return 

        node1.val = val2
        node2.val = val1
        return

    def searchNode(self, root, val):
        if root == None:
            return None

        if root.val == val:
            return root
        left = self.searchNode(root.left, val)
        right = self.searchNode(root.right, val)
        
        if left != None:
            return left
        if right != None:
            return right
        return None

    def inOrder(self, root, res):
        if root == None:
            return 
        
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
        return 

    def searchOuter(self, nums):
        res = []
        pre = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur < pre:
                res.append((pre, cur))

            pre = cur

        return res

import random
nums = list(range(10))
exchange = [0,0]
while exchange[0] == exchange[1]:
    for i in range(2):
        exchange[i] = random.choice(nums)

# print(exchange)
tmp = nums[exchange[0]]
nums[exchange[0]] = nums[exchange[1]]
nums[exchange[1]] = tmp
print(nums)

so = Solution()
outer = so.searchOuter(nums)
print(outer[0][0], outer[1][1])
