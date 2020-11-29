class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# 
# @param root TreeNode类 
# @param o1 int整型 
# @param o2 int整型 
# @return int整型
#
class Solution:
    # s1
    # def lowestCommonAncestor(self , root , o1 , o2 ):
    #     # write code here
    #     child2Parent = {}
    #     self.treeIdx(root, child2Parent)
    #     # return child2Parent
    #     path1, path2 = [],[]
    #     t1 , t2 = o1, o2
    #     while t1 != root.val :
    #         path1.append(t1)
    #         t1 = child2Parent[t1]
    
    #     while t2 != root.val :
    #         path2.append(t2)
    #         t2 = child2Parent[t2]
        
    #     res = root.val
    #     while len(path1)>0 and  len(path2)>0:
    #         v1 = path1.pop()
    #         v2 = path2.pop()
    #         if v1 == v2:
    #             res = v1
    #         else:
    #             break
    #     return res

    # s2 dfs
    def lowestCommonAncestor(self , root , o1 , o2 ):
        # write code here
        if root == None:
            return None
        if root.val == o1:
            return o1
        if root.val == o2:
            return o2
        
        left = self.lowestCommonAncestor(root.left, o1, o2)
        right = self.lowestCommonAncestor(root.right, o1, o2)
        if left == o1 and right == o2:
            return root.val
        else:
            if  left != None:
                return left
            if right != None:
                return right
            return None
            

        
    def treeIdx(self,root,child2Parent):
        if root == None :
            return 
        val = root.val
        left = root.left
        right = root.right
        if left != None:
            child2Parent[left.val] = val
            self.treeIdx(left, child2Parent)
        if right != None:
            child2Parent[right.val] = val
            self.treeIdx(right, child2Parent)
        return

def initTree(pos, l):
    if pos > len(l):
        return None
    if l[pos-1] == None:
        return None
    root = TreeNode(l[pos-1])
    root.left = initTree(2*pos, l)
    root.right = initTree(2*pos+1, l)
    return root

if __name__ == "__main__":
    nums = [3,5,1,6,2,0,8,None,None,7,4]
    o1, o2 = 5,1
    nums = [27,32,34,19,41,17,18,9,14,44,39,None,None,24,30,None,None,None,2,7,42,28,36,None,None,11,6,None,1,None,None,None,31,16,4,22,33,None,None,None,5,10,15,37,12,8,None,35,3,None,23,21,None,None,None,29,None,None,None,40,None,None,None,None,None,None,None,None,None,13,43,None,None,None,None,None,None,25,20,None,None,38,None,26]
    o1,o2 = 32, 38
    root = initTree(1, nums)
    so = Solution()
    print(so.lowestCommonAncestor(root, o1, o2))