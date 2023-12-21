#! python3
# -*- encoding: utf-8 -*-
'''
@File   : crane-POJ2991.py
@Time   : 2022/04/07 17:33:47
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : N 条线段首位相连,每条线段长度不同,其中length_i = L_i,初始阶段,所有线段从0开始依此向上垂直排开,
    现在有C条指令,指令作用使线段之间产生一定角度的顺时钟旋转,比如指令i,代表 L_i-1 与 L_i 之间旋转 A_i 角度
     eg: n = 2, c = 1, 
        L={10, 5}, 
        S = {1}
        A = {90}
        代表,2个线段,线段2朝着顺时针旋转90度,最终的线段顶端的坐标为 (5,10) 即为所求
                

'''
import math

class Crane:
    """
    可以将每个线段视作一个向量,最终的结果实际上是,所有线段代表的向量的求和向量的坐标
    一个难点是,旋转会令一段连续的向量序列的值发生变化,这恰好符合线段树区间修改的API,
    同时最终所求的向量和,也是线段树可以得到的区间信息,
    剩下的就是如果恰当的表达向量的加
    """
    def __init__(self, n,c,l,s,a) -> None:
        self.n = n
        self.c = c
        self.l = l
        self.s = s
        self.a = a
        self.vx = {}
        self.vy = {}
        self.ang = {}

    def build(self, p, left, right):
        """
        节点索引 p,以及其代表的区间 [left, right)
        目的是初始化,所有需要的值 vx, vy, ang
        """
        self.vx[p] = 0
        self.ang[p] = 0
        if left == right-1:
            self.vy[p] = self.l[left]
            return
        mid = left + (right-left)//2
        chdleft = 2*p+1
        chdright = 2*p+2
        self.build(chdleft, left, mid)
        self.build(chdright, mid, right)
        self.vy[p] = self.vy[chdleft]+self.vy[chdright]
        return 

    def change(self ,q , r, p, left, right ):
        """
        q 是 1-based,而 p 是 0-based,相当于q 代表的是 需要旋转的起始节点,节点q-1和 节点q开始逆时针旋转指定角度 r, 
        实际上就是将 节点q 和 角度r 转换成常规 chgleft, chgright, chgval,且要遵循向量加法
        向量a : (x_a, y_a) 向量b: (x_b, y_b)
        向量c 为 向量a+向量b_逆时针旋转r
        那么c的和公式为: ( x_a + (cosr * x_b - sinr * y_b)  ,
                         y_a + (sinr * x_b + cosr * y_b)   )
        """
        # 如果旋转节点q不在p所在的区间段，那么无需做处理
        if q <= left:
            return 
        if q < right:
            mid = left + (right-left)//2
            chdleft = 2*p+1
            chdright = 2*p+2
            self.change(q,r, chdleft, left, mid)
            self.change(q,r, chdright, mid, right)
            # 根据递归原则, chdleft, chdright 已经算出,作为2个单独的向量存在,此时应该要做的操作就是合并 2个向量,成为一个新向量返回,
            # 但是合并过程有一个关键要素是,判断 右向量 chdright 是否需要旋转
            # 如果旋转中心在 mid 左边,那代表 chdright 全部都需要旋转,则应当将旋转角度累计进来；
            # 且left：[q,mid) 理应旋转的部分,也在合并 chdleft内部已经完成,无需单独处理
            # 如果旋转中心在 mid 右边,那代表 chdright 内部合并过程已经完成旋转累计,无需单独处理
            if q<=mid:
                self.ang[p] += r

            sin = math.sin(self.ang[p])
            cos = math.cos(self.ang[p])
            self.vx[p] = self.vx[chdleft] + (cos * self.vx[chdright] - sin * self.vy[chdright])
            self.vy[p] = self.vy[chdleft] + (sin * self.vx[chdright] + cos * self.vy[chdright])
            return

    def solve(self):
        self.build(0, 0, self.n)
        # 可能会出现同一个线段，旋转多次，那么久需要保持每个线段当前的角度
        crt = [math.pi] * self.n # 每个线段初始的角度为 逆时针 180度，这里用弧度表示
        
        for i in range(self.c):
            q = self.s[i]
            r = self.a[i] / 360 * 2 * math.pi - 2*math.pi + crt[i]# 注意，这里是顺时针，需要转换成逆时针
            self.change(q, r, 0, 0, self.n)
            crt[i] = r
            print(f'i: {i} : ({self.vx[0]},{self.vy[0]})')
        return

n=2
c=1
l=[10,5]
s=[1]
a=[90]

n=3
c=2
l = [5,5,5]
s = [1,2]
a = [270, 90]
cr = Crane(n,c,l,s,a)
cr.solve()