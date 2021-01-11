# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        cur = head
        root = None
        while cur!=None:
            post = cur.next
            cur.next = None
            root = self.insertSort(root, cur)
            cur = post
        return root

    def insertSort(self,root, node):
        if root==None or node.val < root.val:
            node.next = root
            return node
    
        cur = root
        while cur.next != None and cur.next.val < node.val:
            cur = cur.next
        
        tmp = cur.next
        cur.next = node
        node.next = tmp
        return root

        