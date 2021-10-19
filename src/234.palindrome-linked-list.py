#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (43.21%)
# Likes:    5810
# Dislikes: 454
# Total Accepted:    700.6K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """"
        回文字符串 重点是寻找mid，然后进行 回文验证
        Follow Up: time O(n) space O(1) 需要一点技巧
        

        1，可以设置2个指针，每次循环(1)走 1 step and 2 step ，这样就可以寻找mid
        2，同时在循环(1)中设置计数器，得到字符长度length
        3, 验证的时候，根据length奇偶不同，设置不同的验证起点，
            但是由于回文字符是反向验证的，linkList 的方向不同
            解决办法是可以把head-mid 之间的linkList 的指针进行逆序操作
            同样也可以在循环(1)中进行

        """
        if head==None:
            return False
        head1 = head
        pre1 = None
        head2 = head
        length = 1
        while head2!=None and head2.next!=None:
            # 循环（1）：逆序，计数，同时设置不同step
            # 注意由于 head1 需要逆指针操作，所以head2需要先运行，负责被head1的逆指针干扰
            head2 = head2.next.next
            length += 2
                    
            post1 = head1.next
            head1.next = pre1
            pre1 = head1
            head1 = post1

        # 修正 length 为 偶数的时候，重复计数的情况
        if head2 == None:
            length -= 1
        
        if length%2==0:
            check1 = pre1
            check2 = head1
        else:
            check1 = pre1
            check2 = head1.next
        while check1!=None and check2!=None:
            if check1.val != check2.val:
                return False
            check1=check1.next
            check2=check2.next
        return True
# @lc code=end

