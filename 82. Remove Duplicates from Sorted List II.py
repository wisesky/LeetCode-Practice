# Definition for singly-linked list.
import re
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def initListNodes(nums):
    head = ListNode()
    node = head
    for num in nums:
        tmp = ListNode(num)
        node.next = tmp
        node = tmp
    return head.next

def printNodes(head):
    node = head
    while node != None:
        print(node.val)
        node = node.next
    return

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        root = ListNode(float('inf'))
        root.next = head
        cur = head
        pre = root
        while cur != None and cur.next != None:
            if cur.val != cur.next.val:
                pre = cur
                cur = cur.next
            else:
                while cur.next != None and cur.val == cur.next.val :
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
                # pre = cur
        # head = root.next
        return root.next

    def test(self, head):
        head.next = None
        return

if __name__ == '__main__':
    so = Solution()
    nums = [1,2,3,3,4,4,5]
    # nums = [1,1,1,2,3]
    head = initListNodes(nums)
    printNodes(head)
    print('*'*50)
    head = so.deleteDuplicates(head)
    # so.test(head)
    printNodes(head)