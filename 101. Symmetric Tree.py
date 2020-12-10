# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        return self.helper(root.left, root.right)

    def helper(self, head1, head2):
        if head1 == None and head2 == None:
            return True
        if head1 == None or head2 == None:
            return False

        if head1.val != head2.val :
            return False
        
        # b1 = self.helper(head1.left, head2.left) and self.helper(head1.right, head2.right)
        b2 = self.helper(head1.left, head2.right) and self.helper(head1.right, head2.left)

        return  b2


def initTree(pos, nums):
    if pos > len(nums):
        return None
    if nums[pos-1] == None:
        return None

    root = TreeNode(nums[pos-1])
    root.left = initTree(2*pos, nums)
    root.right = initTree(2*pos+1, nums)
    return root

nums = [1,2,2,3,4,4,3]
nums = [1,2,2,None,3,None, 3]
root = initTree(1, nums)

so = Solution()
print(so.isSymmetric(root))

        
            

        

