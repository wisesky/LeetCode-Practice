"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node2idx = {}
        cur = head
        cur_idx = 0
        while cur != None:
            node2idx[cur] = cur_idx
            cur = cur.next
            cur_idx += 1

        idx2newNode = {}
        newHead = self.clone(head,node2idx, 0, idx2newNode)
        return newHead

    def clone(self, node, node2idx, idx,idx2newNode):
        if node == None:
            return None
        # if idx in idx2node:
        #     return val2node[idx]

        newNode = Node(node.val)
        idx2newNode[idx] = newNode

        newnode_next = self.clone(node.next, node2idx, idx+1, idx2newNode)
        newNode.next = newnode_next

        random_idx = node2idx.get(node.random)
        newNode.random = None if node.random == None else idx2newNode.get(random_idx)
        
        return newNode