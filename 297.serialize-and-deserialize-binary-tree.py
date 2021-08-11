#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (51.39%)
# Likes:    4821
# Dislikes: 214
# Total Accepted:    480.7K
# Total Submissions: 935.3K
# Testcase Example:  '[1,2,3,None,None,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,None,None,4,5]
# Output: [1,2,3,None,None,4,5]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: root = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# 
# 
#
class TreeNode(object):
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    思路比较直接，利用二叉树 inOrder preOrder 即可还原出唯一二叉树
    但是实现过程中，很多细节有点无所适从，特别是定义数据结构的存储形式的时候，没有一个系统的思考可能出现的input output
    比如，保存inOrder preOder的顺序，采用什么分隔符，唯一标识TreeNode的并不是像教材中用val唯一
    而是有重复的val，那么就需要自定义唯一标识TreeNode 同时还要保证能在inOder preOrder中通用
    目前采用的是 std:id,其实完全可以采用自定义的更简单的标识符，只不过多了一层 id -> self_id -> data 的映射,
    之所以需要self_id 是为了序列化保存数据的时候，减少容量，优化性能
    最终的data结构是:
    ..._rootid=rootval_...
    _ 分隔 root 单元
    = 分割rootid 和 rootval
    | 分割 inOrder preOrder
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        inOrder = self.inOrder(root)
        preOrder = self.preOrder(root)
        return '|'.join([inOrder, preOrder])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        inOrder, preOrder = data.split('|')
        inOrder = inOrder.split('_')
        preOrder = preOrder.split('_')
        return self.order2Node(inOrder, preOrder)

    def order2Node(self, inOrder, preOrder):
        assert len(inOrder) == len(preOrder), 'lenght error'
        if len(inOrder)==0:
            return None
        # root 单元有 空的可能, 即['']
        if preOrder[0] == '':
            return None
        root_id = preOrder[0]
        _, val = root_id.split('=')
        root = TreeNode(val)

        index = inOrder.index(root_id)
        left_inorder = inOrder[ :index]
        right_inorder = inOrder[index+1: ]

        left_length = len(left_inorder)
        left_preorder = preOrder[1:left_length+1]
        right_preorder = preOrder[left_length+1: ]

        left = self.order2Node(left_inorder, left_preorder)
        right = self.order2Node(right_inorder, right_preorder)
        root.left = left
        root.right = right
        return root

    def inOrder(self, root):
        """ in order seq of root
        
        type root: TreeNode
        rtype: str
        """
        if root==None:
            return ''
        root_id = str(id(root)) + '=' + str(root.val)
        left = self.inOrder(root.left)
        right = self.inOrder(root.right)
        return '_'.join([left,root_id, right])

    def preOrder(self, root):
        """pre order seq of root
        
        """
        if root==None:
            return ''

        root_id = str(id(root)) + '=' + str(root.val)
        left = self.preOrder(root.left)
        right = self.preOrder(root.right)
        return '_'.join([root_id , left , right])



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

nums = [1,2,3,None,None,4,5]
nums = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]

def cstTree(i, nums):
    length = len(nums)
    if i >= length:
        return None

    node = TreeNode(nums[i])
    node.left = cstTree(2*i+1, nums)
    node.right = cstTree(2*i+2, nums)
    return node

root = cstTree(0, nums)

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))