#! python3
# -*- encoding: utf-8 -*-
'''
@File   : Dijkstra.py
@Time   : 2023/08/15 18:38:48
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 

Dijkstra 算法

Dijkstra（/ˈdikstrɑ/或/ˈdɛikstrɑ/）算法由荷兰计算机科学家 E. W. Dijkstra 于 1956 年发现，1959 年公开发表。是一种求解 非负权图 上单源最短路径的算法。



将结点分成两个集合：已确定最短路长度的点集（记为 S 集合）的和未确定最短路长度的点集（记为 T 集合）。一开始所有的点都属于 T 集合。

初始化 dis(s)=0，其他点的 dis 均为 +\infty。

然后重复这些操作：

从 T 集合中，选取一个最短路长度最小的结点，移到 S 集合中。
对那些刚刚被加入 S 集合的结点的所有出边执行松弛操作。
直到 T 集合为空，算法结束。

时间复杂度

有多种方法来维护 1 操作中最短路长度最小的结点，不同的实现导致了 Dijkstra 算法时间复杂度上的差异。

暴力：不使用任何数据结构进行维护，每次 2 操作执行完毕后，直接在 T 集合中暴力寻找最短路长度最小的结点。2 操作总时间复杂度为 O(m)，1 操作总时间复杂度为 O(n^2)，全过程的时间复杂度为 O(n^2 + m) = O(n^2)。
二叉堆：每成功松弛一条边 (u,v)，就将 v 插入二叉堆中（如果 v 已经在二叉堆中，直接修改相应元素的权值即可），1 操作直接取堆顶结点即可。共计 O(m) 次二叉堆上的插入（修改）操作，O(n) 次删除堆顶操作，而插入（修改）和删除的时间复杂度均为 O(\log n)，时间复杂度为 O((n+m) \log n) = O(m \log n)。
优先队列：和二叉堆类似，但使用优先队列时，如果同一个点的最短路被更新多次，因为先前更新时插入的元素不能被删除，也不能被修改，只能留在优先队列中，故优先队列内的元素个数是 O(m) 的，时间复杂度为 O(m \log m)。
Fibonacci 堆：和前面二者类似，但 Fibonacci 堆插入的时间复杂度为 O(1)，故时间复杂度为 O(n \log n + m)，时间复杂度最优。但因为 Fibonacci 堆较二叉堆不易实现，效率优势也不够大1，算法竞赛中较少使用。
线段树：和二叉堆原理类似，不过将每次成功松弛后插入二叉堆的操作改为在线段树上执行单点修改，而 1 操作则是线段树上的全局查询最小值。时间复杂度为 O(m \log n)。

在稀疏图中，m = O(n)，使用二叉堆实现的 Dijkstra 算法较 Bellman–Ford 算法具有较大的效率优势；而在稠密图中，m = O(n^2)，这时候使用暴力做法较二叉堆实现更优。


'''
# O(n**2) 暴力实现
class Edge:
    def __init(self, v = 0, w = 0):
        self.v = v
        self.w = w
e = [[Edge() for i in range(maxn)] for j in range(maxn)]
dis = [0x3f3f3f3f] * maxn; vis = [0] * maxn
def dijkstra(n, s):
    dis[s] = 0
    for i in range(1, n + 1):
        u = 0
        mind = 0x3f3f3f3f
        for j in range(1, n + 1):
            if vis[j] == False and dis[v] < mind:
                u = j
                mind = dis[j]
        vis[u] = True
        for ed in e[u]:
            v, w = ed.v, ed.w
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w

# 优先队列实现 O(mlogm)
def dijkstra(e,s):
  '''
  输入：
  e:邻接表
  s:起点
  返回：
  dis:从s到每个顶点的最短路长度
  '''
  dis = defaultdict(lambda:float("inf"))
  dis[s] = 0
  q = [(0,s)]
  vis = set()
  while q:
      _, u = heapq.heappop(q)
      if u in vis: continue
      vis.add(u)
      for v,w in e[u]:
          if dis[v] > dis[u] + w:
              dis[v] = dis[u] + w
              heapq.heappush(q,(dis[v],v))
  return dis
