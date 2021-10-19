"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = []
        self.helper(root, 0, res)
        return root

    def helper(self, root, level, res):
        if root == None:
            return 

        while level >= len(res):
            res.append(None)

        if res[level] != None:
            res[level].next = root
        res[level] = root

        self.helper(root.left, level+1, res)
        self.helper(root.right, level+1, res)
        return
