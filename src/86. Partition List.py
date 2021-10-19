# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # s1
    def partition(self, head: ListNode, x: int) -> ListNode:
        root = ListNode()
        root.next = head
        
        tail = root
        pre = root
        cur = head

        while cur != None and cur.val < x:
            pre = cur
            tail = pre
            cur = cur.next

        while cur != None :
            if cur.val < x:
                pre.next = cur.next
                cur.next = tail.next
                tail.next = cur
                tail = cur

                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        
        return  root.next

    def insertNode(self,root, node):
        pre = root
        cur = root.next
        while cur != None and cur.val < node.val:
            pre = cur
            cur = cur.next
        node.next = cur
        pre.next = node
        return
    
    # s2 题目理解错了，写成了3相快排，且分区还是 插入排序法
    # def partition(self, head: ListNode, x: int) -> ListNode:
    #     root = ListNode()
    #     # root.next = head

    #     equal = ListNode(x)
    #     root.next = equal
    #     equal.next = head
    #     gt = ListNode()

    #     pre = equal
    #     cur = head
    #     while cur != None:
    #         if cur.val == x:
    #             pre = cur
    #             cur = cur.next
    #         elif cur.val < x:
    #             pre.next = cur.next
    #             self.insertNode(root, cur)
    #             cur = pre.next
    #         else: # cur.val > x
    #             pre.next = cur.next
    #             self.insertNode(gt, cur)
    #             cur = pre.next
            
    #     pre.next = gt.next
    #     equal.next = equal.next.next

    #     return root.next
        
def initTree(nums):
    root = ListNode()
    cur = root
    for num in nums:
        node = ListNode(num)
        cur.next = node
        cur = node
    return root.next

def printTree(root):
    cur = root 
    while cur != None:
        print(cur.val)
        cur = cur.next

nums = [1,4,3,2,5,2]
nums = [2,1]
head = initTree(nums)
# printTree(head)
so = Solution()
# so.insertNode(head, ListNode(2))
head = so.partition(head, 2)
printTree(head)

