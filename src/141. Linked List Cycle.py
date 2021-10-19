# Definition for singly-linked list.
from typing import DefaultDict


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        marked = set()

        if head == None:
            return False
        
        cur = head
        while cur != None:
            if id(cur) in marked:
                return True
            marked.add(id(cur))
            cur = cur.next
        return False

