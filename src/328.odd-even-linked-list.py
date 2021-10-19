#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (57.70%)
# Likes:    3690
# Dislikes: 349
# Total Accepted:    416.9K
# Total Submissions: 718.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered
# list.
# 
# The first node is considered odd, and the second node is even, and so on.
# 
# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.
# 
# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# 
# 
# Example 2:
# 
# 
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
# 
# 
# 
# Constraints:
# 
# 
# n == number of nodes in the linked list
# 0 <= n <= 10^4
# -10^6 <= Node.val <= 10^6
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    54ms(7%) 16.3MB(84%)
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        odd.next = head
        even = ListNode()
        even_tail = even

        c = 0
        crt = odd
        while crt.next != None:
            c += 1
            if c%2 == 0:
                even_tail.next = crt.next
                crt.next  = crt.next.next
                even_tail.next.next = None
                even_tail = even_tail.next
            else:
                crt = crt.next
            
        crt.next = even.next
        return odd.next
# @lc code=end

