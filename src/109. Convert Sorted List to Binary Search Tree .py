# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None

        head0 = ListNode()
        head0.next = head
        cur = head
        pre = head0
        mid = head
        flag = 1

        while cur != None:
            if flag == 0:
                pre = mid
                mid = mid.next

            cur = cur.next
            flag = 1 if flag==0 else 0

        pre.next = None

        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head0.next)
        root.right = self.sortedListToBST(mid.next)
        return root
