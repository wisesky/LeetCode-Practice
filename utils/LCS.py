#! python3
# -*- encoding: utf-8 -*-
'''
@File   : LCS.py
@Time   : 2023/08/15 19:20:59
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 
最长公共子序列
给定一个长度为 n 的序列 A 和一个 长度为 m 的序列 B（n,m \leq 5000），求出一个最长的序列，使得该序列既是 A 的子序列，也是 B 的子序列。

设 f(i,j) 表示只考虑 A 的前 i 个元素，B 的前 j 个元素时的最长公共子序列的长度，求这时的最长公共子序列的长度就是 子问题。f(i,j) 就是我们所说的 状态，则 f(n,m) 是最终要达到的状态，即为所求结果。

对于每个 f(i,j)，存在三种决策：如果 A_i=B_j，则可以将它接到公共子序列的末尾；另外两种决策分别是跳过 A_i 或者 B_j。状态转移方程如下：

 
f(i,j)=\begin{cases}f(i-1,j-1)+1&A_i=B_j\\\max(f(i-1,j),f(i,j-1))&A_i\ne B_j\end{cases}


'''


a[n], b[m], f[n][m]

def dp():
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i] == b[j]:
                f[i][j] = f[i-1][j-1] + 1
            else:
                f[i][j] = max(f[i][j-1], f[i-1][j])
    return f[n][m]
