# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        root = pHead
        newRoot = ListNode(-1)
        newRoot.next = root
        cur = root.next
        while cur != None:
            root.next = cur.next
            cur.next = newRoot.next
            newRoot.next = cur
            cur = root.next
        return newRoot.next


def initNode(nums):
    root = ListNode(-1)
    cur = root
    for num in nums:
        newNode = ListNode(num)
        cur.next = newNode
        cur = newNode
    return root.next

l = list(range(10))
root = initNode(l)
so = Solution()
root = so.ReverseList(root)

cur = root
while cur != None:
    print(cur.val)
    cur = cur.next