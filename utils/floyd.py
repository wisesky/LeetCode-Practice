#! python3
# -*- encoding: utf-8 -*-
'''
@File   : floyd.py
@Time   : 2023/08/15 18:25:34
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 

Floyd 算法

是用来求任意两个结点之间的最短路的。

复杂度比较高，但是常数小，容易实现。（我会说只有三个 for 吗？）

适用于任何图，不管有向无向，边权正负，但是最短路必须存在。（不能有个负环）

O(n**3)
'''

#定义一个数组 f[k][x][y]，表示只允许经过结点 1 到 k（也就是说，在子图 V'={1, 2, \ldots, k} 中的路径，注意，x 与 y 不一定在这个子图中），结点 x 到结点 y 的最短路长度。
#f[n][x][y] 就是结点 x 到结点 y 的最短路长度（因为 V'={1, 2, \ldots, n} 即为 V 本身，其表示的最短路径就是所求路径）。
#f[0][x][y]：x 与 y 的边权，或者 0，或者 +\infty（f[0][x][y] 什么时候应该是 +\infty？当 x 与 y 间有直接相连的边的时候，为它们的边权；当 x = y 的时候为零，因为到本身的距离为零；当 x 与 y 没有直接相连的边的时候，为 +\infty）。
#f[k][x][y] = min(f[k-1][x][y], f[k-1][x][k]+f[k-1][k][y])（f[k-1][x][y]，为不经过 k 点的最短路径，而 f[k-1][x][k]+f[k-1][k][y]，为经过了 k 点的最短路）。


for k in range(1,n+1):
    for x in range(1,n+1):
        for y in range(1,n+1):
            # f[k][x][y] = min( f[k-1][x][y], 
            #                   f[k-1][x][k] + f[k-1][k][y]  )
            f[x][y] = min(f[x][y], f[x][k] + f[k][y])