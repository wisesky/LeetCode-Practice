"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def build(vals, idx):
    if len(vals)==0 or idx>=len(vals):
        return None
    root = Node(vals[idx])
    root.left = build(vals,idx*2+1)
    root.right = build(vals,idx*2+2) 
    return root

class Solution:
    # DFS 利用前序遍历的位置来完成层级间的链接
    def connect(self, root: 'Node') -> 'Node':
        pre = []
        self.helper(root, 0, pre)
        return root
    # 可以用前序遍历的方式，得到同一个层级内的，前后排序，那么只要知道当前节点的level，便可以根据先后顺序，建立next链接
    #（实际上，中序和后序，同一个层级内也是按照左右排序的）
    # 前序遍历位置，状态是：（root，root所在level）
    # pre用来存放此level的前一个节点
    def helper(self, root, level, pre):
        # DFS终止条件
        if root == None:
            return 
        # 前序遍历第一次来到此level，那么需要初始化此level头结点
        while level >= len(pre):
            pre.append(None)
        # 同一个level内，先进来的的节点链接到后进来的节点
        if pre[level] != None:
            pre[level].next = root
        # 当前节点作为待链接的pre，入列
        pre[level] = root
        # DFS 下层节点
        self.helper(root.left, level+1, pre)
        self.helper(root.right, level+1, pre)
        return
    
    # Solution_2
    # 同样是遍历DFS，不过无须记录level状态
    # 原以为跨左右节点的链接不容易建立，但是却可以通过构筑再下一层的跨左右节点之间的链接的方式，来递归传递到叶子节点
    # (left, right) -> (left.left, left.right), (left.right, right.left), (right.left, right.right)
    # 关键就是中间的 (left.right -> right.left),这两个节点间的递归操作，可以传递到最底层，所以可以覆盖所有情况
    # 分析出这个DFS模式，还是比较考验总结能力，我模式总结错了，思路虽然正确,但是无法覆盖所有情况
    def connect_2(self, root) :
        if root is None:
            return None
        self.cnt(root.left, root.right)
        return root
    #  链接 left 和 right，以及其子节点之间的链接
    def cnt(self, left, right):
        if left is None or right is None:
            return
        left.next = right
        self.cnt(left.left, left.right)
        self.cnt(left.right, right.left)
        self.cnt(right.left, right.right)
        return 

if __name__ == "__main__":
    vals = list(range(1,8))
    root = build(vals, 0)
    so = Solution()
    # result = so.connect(root)
    result = so.connect_2(root)

    left = result
    while left is not None:
        start = left
        while start is not None:
            print(start.val)
            start = start.next
        print('-'*20)
        left = left.left