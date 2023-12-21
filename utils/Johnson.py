#! python3
# -*- encoding: utf-8 -*-
'''
@File   : Johnson.py
@Time   : 2023/08/15 18:58:53
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : https://oi-wiki.org/graph/shortest-path/#floyd-算法

Johnson 全源最短路径算法
Johnson 和 Floyd 一样，是一种能求出无负环图上任意两点间最短路径的算法。该算法在 1977 年由 Donald B. Johnson 提出。

任意两点间的最短路可以通过枚举起点，跑 n 次 Bellman–Ford 算法解决，时间复杂度是 O(n^2m) 的，也可以直接用 Floyd 算法解决，时间复杂度为 O(n^3)。

注意到堆优化的 Dijkstra 算法求单源最短路径的时间复杂度比 Bellman–Ford 更优，如果枚举起点，跑 n 次 Dijkstra 算法，就可以在 O(nm\log m)（取决于 Dijkstra 算法的实现）的时间复杂度内解决本问题，比上述跑 n 次 Bellman–Ford 算法的时间复杂度更优秀，在稀疏图上也比 Floyd 算法的时间复杂度更加优秀。

但 Dijkstra 算法不能正确求解带负权边的最短路，因此我们需要对原图上的边进行预处理，确保所有边的边权均非负。

一种容易想到的方法是给所有边的边权同时加上一个正数 x，从而让所有边的边权均非负。如果新图上起点到终点的最短路经过了 k 条边，则将最短路减去 kx 即可得到实际最短路。

但这样的方法是错误的。考虑下图：



1 \to 2 的最短路为 1 \to 5 \to 3 \to 2，长度为 −2。

但假如我们把每条边的边权加上 5 呢？



新图上 1 \to 2 的最短路为 1 \to 4 \to 2，已经不是实际的最短路了。

Johnson 算法则通过另外一种方法来给每条边重新标注边权。

我们新建一个虚拟节点（在这里我们就设它的编号为 0）。从这个点向其他所有点连一条边权为 0 的边。

接下来用 Bellman–Ford 算法求出从 0 号点到其他所有点的最短路，记为 h_i。

假如存在一条从 u 点到 v 点，边权为 w 的边，则我们将该边的边权重新设置为 w+h_u-h_v。

接下来以每个点为起点，跑 n 轮 Dijkstra 算法即可求出任意两点间的最短路了。

一开始的 Bellman–Ford 算法并不是时间上的瓶颈，若使用 priority_queue 实现 Dijkstra 算法，该算法的时间复杂度是 O(nm\log m)。

正确性证明

为什么这样重新标注边权的方式是正确的呢？

在讨论这个问题之前，我们先讨论一个物理概念——势能。

诸如重力势能，电势能这样的势能都有一个特点，势能的变化量只和起点和终点的相对位置有关，而与起点到终点所走的路径无关。

势能还有一个特点，势能的绝对值往往取决于设置的零势能点，但无论将零势能点设置在哪里，两点间势能的差值是一定的。

接下来回到正题。

在重新标记后的图上，从 s 点到 t 点的一条路径 s \to p_1 \to p_2 \to \dots \to p_k \to t 的长度表达式如下：

(w(s,p_1)+h_s-h_{p_1})+(w(p_1,p_2)+h_{p_1}-h_{p_2})+ \dots +(w(p_k,t)+h_{p_k}-h_t)

化简后得到：

w(s,p_1)+w(p_1,p_2)+ \dots +w(p_k,t)+h_s-h_t

无论我们从 s 到 t 走的是哪一条路径，h_s-h_t 的值是不变的，这正与势能的性质相吻合！

为了方便，下面我们就把 h_i 称为 i 点的势能。

上面的新图中 s \to t 的最短路的长度表达式由两部分组成，前面的边权和为原图中 s \to t 的最短路，后面则是两点间的势能差。因为两点间势能的差为定值，因此原图上 s \to t 的最短路与新图上 s \to t 的最短路相对应。

到这里我们的正确性证明已经解决了一半——我们证明了重新标注边权后图上的最短路径仍然是原来的最短路径。接下来我们需要证明新图中所有边的边权非负，因为在非负权图上，Dijkstra 算法能够保证得出正确的结果。

根据三角形不等式，图上任意一边 (u,v) 上两点满足：h_v \leq h_u + w(u,v)。这条边重新标记后的边权为 w'(u,v)=w(u,v)+h_u-h_v \geq 0。这样我们证明了新图上的边权均非负。

这样，我们就证明了 Johnson 算法的正确性。
'''
