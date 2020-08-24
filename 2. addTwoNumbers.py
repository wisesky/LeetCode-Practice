# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import ListNode
class Solution:
    # linknode 组成的数字相加 ,而且还是逆序的 234 : 4->3->2
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = l1
        y = l2
        e = 0
        root = ListNode(-1)
        tail = root
        while x != None or y != None:
            xv = x.val if x != None else 0
            yv = y.val if y != None else 0
            res = xv + yv + e
            r = res % 10
            e = res // 10
            rl = ListNode(r)
            tail.next = rl
            tail = rl
            x = x.next if x != None else None
            y = y.next if y != None else None
        if e != 0:
            tail.next = ListNode(1)
        return root.next

    def initFromList(self, li):
        root = ListNode(-1)
        pre = root
        for x in li:
            tmp = ListNode(x)
            pre.next = tmp
            pre = tmp
        return root.next
if __name__ == "__main__":
    so = Solution()
    ln1 = so.initFromList([2,4,3,1,2,3,4])
    ln2 = so.initFromList([5,6,4,4,3,2,1])
    rst = so.addTwoNumbers(ln1, ln2)
    while rst != None:
        print(rst.val)
        rst = rst.next
