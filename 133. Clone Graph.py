"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        val2node = {}
        root = self.clone(node, val2node)
        return root

    def clone(self, node, val2node):
        if node == None:
            return None
        if node.val in val2node:
            return val2node[node.val]

        newNode = Node(node.val)
        val2node[node.val] = newNode
        for neigh in node.neighbors:
            newNeigh = self.clone(neigh, val2node)
            # val2node[neigh.val] = newNeigh
            newNode.neighbors.append(newNeigh)
        
        return newNode
