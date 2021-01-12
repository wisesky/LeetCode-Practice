# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        # call quick3way
        # root = ListNode()
        # root.next = head
        # root, tail = self.quick3Way(root)
        # return root.next
        
        # 这里 mid, tail 是作为分割 nums 用，所以设为不同的起点
        # nums[lo..mid..hi] 一样， 只是linknode 无法实现O(1)的元素访问，
        # 采用不同步幅的方法分割，之前tail=head 回导致无限循环，使得 nums[ :2] 永远被分为 nums[0:2] , None
        mid, tail = head, head.next
        while tail and tail.next:
            tail = tail.next.next
            mid = mid.next
        start = mid.next
        mid.next = None
        left, right = self.sortList(head), self.sortList(start)
        return self.mergeSort(left, right)

    # with head None Node
    # in-place change
    # return tail node
    def quick3Way(self, root):
        if root.next == None :
            return root, root
        if root.next.next == None:
            return root, root.next

        
        left = ListNode()
        left_tail = left
        right = ListNode()
        right_tail = right
        equal = ListNode()

        cur = root.next
        equal_val = cur.val
        while cur != None:
            post = cur.next
            cur.next = None
            if cur.val == equal_val:
                cur.next = equal.next
                equal.next = cur
            elif cur.val < equal_val:
                # cur.next = left.next
                # left.next = cur
                left_tail.next = cur
                left_tail = cur
            else: # cur.val > equal_val
                # cur.next = right.next
                # right.next = cur
                right_tail.next = cur
                right_tail = cur
            cur = post
        
        left, newLeftTail = self.quick3Way(left)
        right, newRightTail = self.quick3Way(right)
        # root = left 
        # tail = left
        # while tail.next != None:
        #     tail = tail.next
        tail = newLeftTail
        tail.next = equal.next
        while tail.next != None:
            tail = tail.next
        tail.next = right.next
        
        return left, newRightTail if right.next!=None else tail

    def mergeSort(self, l1, l2):
        root = ListNode()
        tail = root
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return root.next


def initNodes(nums):
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

nums = [4,3,1,2]
# nums = [-1,5,3,4,0]
root = initNodes(nums)
# printNodes(root)

so = Solution()
root = so.sortList(root)
printNodes(root)