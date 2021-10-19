# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = ListNode()
        root.next = head

        i = 1
        pre = root
        cur = head
        while cur != None and i < m:
            pre = cur
            cur = cur.next
            i += 1

        tail = pre
        rev_tail = cur

        while cur != None  and i <= n :
            tmpNode = cur.next
            cur.next = pre

            pre = cur
            cur = tmpNode
            i += 1
        
        tail.next = pre
        rev_tail.next = cur

        return root.next

def initTree(nums):
    root = ListNode()
    cur = root

    for num in nums:
        node = ListNode(num)
        cur.next = node
        cur = node
    return root.next

def printTree(root ):
    cur = root
    while cur != None:
        print(cur.val)
        cur = cur.next

nums = [1,2,3,4, 5]
head = initTree(nums)
# printTree(head)

so = Solution()
head = so.reverseBetween(head, 1, 5)
printTree(head)