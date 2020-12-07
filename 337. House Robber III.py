# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, root: TreeNode) -> int :
        return max(self.helper(root, True), self.helper(root, False))
    
    def helper(self, node, chosen=True):
        if node == None:
            return 0
        if self.memo.get((id(node), chosen)) != None:
            return self.memo[id(node), chosen]
        if chosen == True:
            leftSum = self.helper(node.left, chosen=False)
            rightSum = self.helper(node.right, chosen=False)
            self.memo[id(node), chosen] = leftSum + node.val + rightSum
            # return self.memo[node, chosen]
        else:
            # left only
            leftSum = max(self.helper(node.left, chosen=True) , self.helper(node.left, chosen=False))
            # right only
            rightSum = max(self.helper(node.right, chosen=True), self.helper(node.right, chosen=False))
            self.memo[id(node), chosen] = leftSum + rightSum
            # return leftSum + rightSum

        return self.memo[id(node), chosen]
    



def initTree(pos, ls):
    if pos > len(ls):
        return None
    if ls[pos-1] == None:
        return None
    root = TreeNode(ls[pos-1])
    root.left = initTree(2*pos, ls)
    root.right = initTree(2*pos+1, ls)
    return root


def preOrder(root):
    if root == None:
        # print('null')
        return
    preOrder(root.left)
    print(root.val)
    preOrder(root.right)
    return

if __name__ == "__main__":
    # l = [1,2,3,None,4,None,5]
    l = [1,2,3,None,4,None,5]
    # l = [1]
    root = initTree(1,l)
    preOrder(root)

    # so = Solution()
    # reslult = so.rob(root)
    # print(reslult)


