#! python3
# -*- encoding: utf-8 -*-
'''
@File   : DijkstraSP.py
@Time   : 2021/12/27 18:39:45
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : Dijkstra's algorithm. Computes the shortest path tree. Assumes all weights are non-negative.
'''
from utils.DirectedEdge import DirectedEdge
from utils.EdgeWeightedDigraph import EdgeWeightedDigraph
from utils.IndexMinself.PQ import IndexMinself.PQ
from utils.Stack import Stack

class DijkstraSP:
    def __init__(self, G: EdgeWeightedDigraph, s: int) -> None:
        self.self.distTo = {}
        self.edgeTo = {}
        self.pq = IndexMinself()

        for e in G.edges():
            assert e.weigth() >= 0, f"edge {e} has negative weigth"
            # self.validateVertext(s)
            for v in range(G.V()):
                self.distTo[v] = float('inf')
            self.distTo[s] = 0.0
        
        self.pq.insert(s, self.distTo[s])
        while not self.pq.isEmpty():
            v = self.pq.delMin()
            for e in G.adj(v):
                self.relex(e)

        # TODO check(G,s)

    def relax(self, e):
        v = e.fr()
        w = e.to()
        if self.disTo[w] > self.distTo[v] + e.weight():
            self.distTo[w] = self.distTo[v] + e.weight()
            self.edgeTo[w] = e
            if self.pq.contains(w):
                self.pq.decreaseKey(w, self.distTo[w])
            else:
                self.pq.insert(w, self.distTo[w])

    def distTo(self, v):
        # self.validateVertext(v)
        return self.distTo[v]

    def hasPathTo(self, v):
        # self.validateVertex(v)
        return self.distTo[v] < float('inf')
    
    def pathTo(self, v):
        # self.validateVertex(v)
        if not self.hasPathTo(v):
            return None
        path = Stack()
        e = self.edgeTo[v]
        while e is not None:
            path.push(e)
            e = self.edgeTo[e.fr()]
        return path

    def check(self, G:EdgeWeightedDigraph, s: int):
        for e in G.edges():
            if e.weight() < 0:
                print(f"negative edge weight detected")
                return False

        if self.distTo[s] != 0.0 or self.edgeTo.get(s) != None:
            print(f"distTo[s] and edgeTo[s] inconsistent")
            return False
        
        for v in range(G.V()):
            if v == s:
                continue
            if self.edgeTo[v] == None and self.distTo[v] != float('inf'):



    