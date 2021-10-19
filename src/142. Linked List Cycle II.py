# Definition for singly-linked list.
# from typing import DefaultDict

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        marked = {}

        if head == None:
            return -1
        
        cur = head
        # pos = 0
        while cur != None:
            if id(cur) in marked:
                return marked[id(cur)]
            marked[id(cur)] = cur
            cur = cur.next
            # pos += 1
        return -1

