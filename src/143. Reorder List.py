# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return 

        mid, tail = head, head
        pre = None
        isEven = False
        backLink = {id(head):None}
        while tail.next != None:
            pre = mid
            mid = mid.next
            backLink[id(mid)] = pre
            if tail.next.next == None:
                isEven = True
                tail = tail.next
            else:
                tail = tail.next.next

        newTail = mid
        if isEven:
            pre = backLink[id(pre)]
        while pre!=None and newTail.next!=None:
            post = newTail.next
            newTail.next = post.next
            post.next = pre.next
            pre.next = post
            pre = backLink[pre]

        return 

def initRoot(nums):
    root = ListNode()
    cur = root
    for num in nums:
        node = ListNode(num)
        cur.next = node
        cur = node
    return root.next

def printNodes(root):
    cur = root 
    while cur!=None:
        print(cur.val)
        cur = cur.next
    return

nums = [1,2,3,4]
root = initRoot(nums)
# printNodes(root)
so = Solution()
so.reorderList(root)
printNodes(root)