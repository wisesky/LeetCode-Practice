# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def initFromList(self,nums):
        head = ListNode(-1)
        last = head
        for num in nums:
            node = ListNode(num)
            last.next = node
            last = node
        return head.next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 0
        cur = head
        while cur != None:
            cur = cur.next
            length += 1
        if length == 0:
            return None
        if length ==1 :
            return head
        
        left = k % length
        for _ in range(left):
            head = self.rotateOne(head)

        return head

    def rotateOne(self, head):
        if head == None or head.next == None:
            return head

        pre = head
        cur = pre.next
        while cur.next != None:
            pre = cur
            cur = cur.next

        pre.next = None
        cur.next = head
        head = cur

        return head

so = Solution()
nums = list(range(1,6))
k = 2
head = ListNode().initFromList(nums)

head = so.rotateRight(head, k)

cur = head
while cur != None:
    print(cur.val)
    cur = cur.next