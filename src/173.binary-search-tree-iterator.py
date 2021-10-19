#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.head = TreeNode(float('-inf'), left=None, right=None)
        self.head.right = self._transform(root)

    def _transform(self, root:TreeNode):
        # tree -> linklist
        if root == None:
            return None
        leftHead = self._transform(root.left)
        rightHead = self._transform(root.right)
        leftTail = leftHead
        while  leftTail != None and leftTail.right != None:
            leftTail = leftTail.right
        
        if leftTail != None:
            leftTail.right = root
        root.right = rightHead
        return leftHead if leftHead!=None else root

    def next(self) -> int:
        if self.head.right == None:
            return None
        self.head = self.head.right
        return self.head.val

    def hasNext(self) -> bool:
        return self.head.right != None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

