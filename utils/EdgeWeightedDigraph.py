#! python3
# -*- encoding: utf-8 -*-
'''
@File   : EdgeWeightedDigraph.py
@Time   : 2021/12/27 18:39:02
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : An edge-weighted digraph, implemented using adjacency lists.
'''

from DirectedEdge import DirectedEdge
from Bag import Bag
from collections import defaultdict

class EdgeWeightedDigraph:
    """
    有向加权图
    """
    def __init__(self, edgesList=[]) -> None:
        self.adj = defaultdict(Bag)
        self.indegree = defaultdict(lambda :0)
        self.numOfVertics = 0
        self.numOfEdges = 0
        for e in edgesList:
            self.addEdge(e)

    def V(self):
        return self.numOfVertics

    def E(self):
        return self.numOfEdges

    def validateVertice(self, vertice):
        """
        教材实现限定 v in [0, V]
        这里不做限制
        """
        return True

    def addEdge(self, e: DirectedEdge):
        v = e.fr()
        w = e.to()
        assert self.validateVertice(v) and self.validateVertice(w), \
                f"vertice {w} or {v} not validate"
        if v not in self.adj and v not in self.indegree:
            self.numOfVertics += 1
        if w not in self.adj and w not in self.indegree:
            self.numOfVertics += 1
        self.adj[v].add(e)
        self.indegree[w] += 1
        self.numOfEdges += 1
        

    def adj(self, v):
        # return iter(self.ajd[v])
        return self.adj[v]

    def edges(self):
        """
        懒惰实现
        """
        edges_list = []
        for v in self.adj:
            edges_list.extend(self.adj[v])
        return edges_list

    def __str__(self):
        out_str = [f"Graph got {self.numOfVertics} vertices {self.numOfEdges} edges : "]
        for e in self.edges():
            out_str.append(str(e))
        return '\n'.join(out_str)

if __name__=='__main__':
    edgesList = [
        DirectedEdge(1,2,1),
        DirectedEdge(2,3,2) ,
        DirectedEdge(3,4,3) ,
        DirectedEdge(5,6,2) ,
        DirectedEdge(3,2,2) ,
        ]
    g = EdgeWeightedDigraph(edgesList)
    print(g)