#! python3
# -*- encoding: utf-8 -*-
'''
@File   : Bellman-Ford.py
@Time   : 2023/08/15 18:28:58
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 

Bellman–Ford 算法是一种基于松弛（relax）操作的最短路算法，可以求出有负权的图的最短路，并可以对最短路不存在的情况进行判断。

对于边 (u,v)，松弛操作对应下面的式子：dis(v) = \min(dis(v), dis(u) + w(u, v))。

Bellman–Ford 算法所做的，就是不断尝试对图上每一条边进行松弛。我们每进行一轮循环，就对图上所有的边都尝试进行一次松弛操作，当一次循环中没有成功的松弛操作时，算法停止。

O(mn)
'''

class Edge:
    def __init__(self, v=0, w=0) -> None:
        self.v = v
        self.w = w

e = [[Edge() for i in range(maxn)] for j in range(maxn)]
dis = [0x3f3f3f3f] * maxn
# 判断负环
def bellmanford(n , s):
    dis[s] = 0
    for i in range(1, n+1):
        flag = False
        for u in range(1, n+1):
            for ed in e[u]:
                v, w  = ed.v, ed.w
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] = W
                    flag = True
                # 没有可以松弛的边时就停止算法
                if flag is False :
                    break
        # 第 n 轮循环仍然可以松弛时说明 s 点可以抵达一个负环
        return flag


# 队列优化 SPFA

"""Shortest Path Faster Algorithm。

很多时候我们并不需要那么多无用的松弛操作。

很显然，只有上一次被松弛的结点，所连接的边，才有可能引起下一次的松弛操作。

那么我们用队列来维护「哪些结点可能会引起松弛操作」，就能只访问必要的边了。

SPFA 也可以用于判断 s 点是否能抵达一个负环，只需记录最短路经过了多少条边，当经过了至少 n 条边时，说明 s 点可以抵达一个负环。"""

class Edge:
    def __init__(self, v = 0, w = 0):
        self.v = v
        self.w = w

e = [[Edge() for i in range(maxn)] for j in range(maxn)]
dis = [0x3f3f3f3f] * maxn; cnt = [0] * maxn; vis = [0] * maxn

q = []
def spfa(n, s):
    dis[s] = 0
    vis[s] = 1
    q.append(s)
    while len(q) != 0:
        u = q[0]
        vis[u] = 0
        q.pop()
        for ed in e[u]:
            v, w  = ed.v, ed.w
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                cnt[v] = cnt[u] + 1 # 记录最短路经过的边数
                if cnt[v] >= n:
                    return False
                # 在不经过负环的情况下，最短路至多经过 n - 1 条边
                # 因此如果经过了多于 n 条边，一定说明经过了负环
                if vis[v] == False:
                    q.append(v)
                    vis[v] = True
