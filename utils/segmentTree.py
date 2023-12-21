#! python3
# -*- encoding: utf-8 -*-
'''
@File   : segmentTree.py
@Time   : 2022/04/07 12:06:30
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
@Desc   : 以堆的方式维护区间信息的数据结构，可以在O(logN)的时间复杂度内，实现
        1. 单点修改
            单点修改，则跟堆类似，单点信息的变更，会递归向上修改区间信息，
        2. 区间查询
            核心算法在于区间查询 [qryleft, qryright) 与 节点p代表的区间 [left, right) 有重合的时候，可以利用递归查询p的左儿子 + 右儿子节点，
        这样，就可以得到查询 [qryleft, qryrigfht）重合的那部分区间信息，过滤掉不重合的部分，即可快速得到区间信息
        3. 区间修改（lazy）
            常规的区间修改，会遍历区间所有节点，频繁的修改，时间复杂度急剧上升；一种较好的应对手段是，延迟更新修改，因为针对一个区间的修改，可以迅速更新区间的信息，
            而不必递归的更新到儿子节点，待到下次有其他的操作需要用到儿子节点的时候，再执行儿子节点的区间修改操作，但是仍然不更新儿子节点的子节点。
        Tips:
            1.建堆，可以循环用单点修改来增添值，但是递归的更新是更有效的建堆方法
            2.无需纠结完美二叉树 还是 完全二叉树的问题，只要保证索引符合节点和子节点的关系即可，在建树阶段，可以实现近乎完美的平衡二叉树切分，
            那么只需要利用二分法切割，就算索引太大，造成列表稀疏的问题，仍然可以用 dict 来解决，因为并不需要保证 dict 连续的索引必须要有值。
        例题: crane-POJ2991.py
'''
import math
class segmentTree:
    """
    求和线段树， 完美二叉树版本，即 叶子结点树木是满的
    所有的nums的值都位于 叶子结点， 而且二叉树的每一层的节点个数都是偶数
    """
    def __init__(self, nums) -> None:
        """
        d: 线段树数组 0-based
        nums: 索引 0-based
        """
        length = len(nums)
        n = 1
        # 为了获得完美二叉树， 叶子节点数目必须是2的幂
        while n<length:
            n *= 2
        self.a = nums
        self.n = n
        self.d = [0] * (2*n-1)
        # s1 : 迭代建树
        # for i in range(length):
        #     self.update(i, nums[i])
        # s2 ： 递归建树
        self.build(0, n, 0)

    def update(self, i, val):
        """
        i: 0-based
        p: 0-based
        相当于数组 nums[i] = val
        那么就需要修改二叉树关联所有值，类似于 堆中的 swim
        """
        p = i + self.n - 1
        self.d[p] = val
        while p > 0:
            p = (p-1) // 2
            self.d[p] = self.d[2*p+1] + self.d[2*p+2]
     
    def build(self, left, right, p):
        """
        p: 0-based 区间编号 代表区间 [left, right)
        """
        if left == right-1:
            self.d[p] = self.a[left] if left < len(self.a) else 0
            return
        mid = left + (right - left)//2
        self.build(left, mid, 2*p+1)
        self.build(mid, right, 2*p+2)
        self.d[p] = self.d[2*p+1] + self.d[2*p+2]
        return

    def getSum(self, lo, hi, s, t, p):
        """
        [lo, hi] 为查询区间， [s,t]为当前节点包含的区间， p为当前节点编号，0-based
        """
        if lo <= s and hi >= t:
            return self.d[p]
        
        mid = s + (t-s)//2
        sm = 0
        if lo <= mid :
            sm += self.getSum(lo, hi, s, mid, p*2+1)
        if hi > mid:
            sm += self.getSum(lo, hi, mid+1, t, p*2+2)
        return sm


class segmentTree:
    """
    非完美二叉树版本， 即二分法分割区间
    """
    def __init__(self, nums) -> None:
        """
        p 代表 [left, right) 
        eg:
            0 -> [0, length)
            1 -> [0, mid)
            2 -> [mid, length)
        注意， 这里d的数据类型dict是更优选择， 因为对nums 进行递归的二分法分割区间，本质上，索引仍然是连续的，只不过在dict不占用空间
        如果用list，这个索引必须有值
        如果用dict， 则会节省很多索引空间
        eg:
                 21
             6       15
            1  5    4   11
              2 3      5  6
        切分mid+1，则可以把切分点右移一位
                21
             6       15
            3  3    9   6
           1 2     4 5   
        """
        length = len(nums)
        # self.d = [0] * (2*length-1)
        self.d = {}
        self.a = nums
        self.build(0, length, 0)

    def build(self, left, right, p):
        """
        p 代表 [left, right)
        """
        if left == right-1:
            self.d[p] = self.a[left]
            return
        mid = left + (right-left)//2
        chdleft = 2*p+1
        chdright = 2*p+2
        self.build(left, mid, chdleft)
        self.build(mid, right, chdright)

        self.d[p] = self.d[chdleft] + self.d[chdright]
        return

    def change(self, chgleft, chgright, chgval, left, right, p):
        """
        修改区间 [chgleft, chgright) , 区间内每个val都加上 chgval
        p代表区间[left, right)
        """
        if chgleft >= right or chgright <= left:
            return
        if left == right-1:
            self.d[p] += chgval
            return

        mid = left + (right-left)//2
        chdleft = 2*p+1
        chdright = 2*p+2
        self.change(chgleft, chgright, chgval, left, mid, chdleft)
        self.change(chgleft, chgright, chgval, mid, right, chdright)
        self.d[p] = self.d[chdleft] + self.d[chdright]
        return
        
    def getSum(self, qryleft, qryright, left, right, p):
        """
        查询区间[qryleft, qryright)
        p代表区间[left, right)
        """
        if qryleft >= right or qryright <= left:
            return 0
        if qryleft <= left and qryright >= right:
            return self.d[p]

        mid = left + (right-left)//2
        chdleft = 2*p + 1
        chdright = 2*p + 2
        chdleftSum = self.getSum(qryleft, qryright, left, mid, chdleft)
        chdrightSum = self.getSum(qryleft, qryright, mid, right, chdright)
        return chdleftSum + chdrightSum

class lazySegmentTree:
    """
    非完美二叉树版本， 即二分法分割区间, lazy更新值

    """
    def __init__(self, nums) -> None:
        """
        p 代表 [left, right) 
        eg:
            0 -> [0, length)
            1 -> [0, mid)
            2 -> [mid, length)
        注意， 这里d的数据类型dict是更优选择， 因为对nums 进行递归的二分法分割区间，本质上，索引仍然是连续的，只不过在dict不占用空间
        如果用list，这个索引必须有值
        如果用dict， 则会节省很多索引空间
        eg:
                 21
             6       15
            1  5    4   11
              2 3      5  6
        切分mid+1，则可以把切分点右移一位
                21
             6       15
            3  3    9   6
           1 2     4 5   
        """
        length = len(nums)
        # self.d = [0] * (2*length-1)
        self.d = {}
        self.mark = {}
        self.a = nums
        self.build(0, length, 0)

    def build(self, left, right, p):
        """
        p 代表 [left, right)
        """
        if left == right-1:
            self.d[p] = self.a[left]
            return
        mid = left + (right-left)//2
        chdleft = 2*p+1
        chdright = 2*p+2
        self.build(left, mid, chdleft)
        self.build(mid, right, chdright)

        self.d[p] = self.d[chdleft] + self.d[chdright]
        return

    def change(self, chgleft, chgright, chgval, left, right, p):
        """
        修改区间 [chgleft, chgright) , 区间内每个val都加上 chgval
        p代表区间[left, right)
        """
        if left == right-1:
            self.d[p] += chgval
            return
        if chgleft >= right or chgright <= left:
            return 
        if chgleft <= left and chgright >= right:
            self.d[p] += chgval * (right - left)
            self.mark[p] = self.mark.get(p, 0) + chgval
            return
        if self.mark.get(p) is not None:
            self.sink(left, right, p)
        
        mid = left + (right-left) // 2
        chdleft = 2*p + 1
        chdright = 2*p + 2
        self.change(chgleft, chgright, chgval, left, mid, chdleft)
        self.change(chgleft, chgright, chgval, mid, right, chdright)
        self.d[p] = self.d[chdleft] + self.d[chdright]
        return

    def getSum(self, qryleft, qryright, left, right, p):
        """
        查询区间[qryleft, qryright)
        p代表区间[left, right)
        """
        if qryleft >= right or qryright <= left:
            return 0
        if qryleft <= left and qryright >= right:
            return self.d[p]
        if self.mark.get(p) is not None:
            self.sink(left, right, p)
        
        mid = left + (right-left)//2
        chdleft = 2*p+1
        chdright = 2*p+2
        leftSum = self.getSum(qryleft, qryright, left, mid, chdleft)
        rightSum = self.getSum(qryleft, qryright, mid, right, chdright)
        return leftSum + rightSum
    
    def sink(self, left, right, p):
        """
        有lazy标记的节点，需要下传值
         p -> [left, right)
        """
        if left == right - 1:
            self.mark.pop(p)
            return

        chgval = self.mark.pop(p)
        mid = left + (right-left)//2
        chdleft = 2*p + 1
        chdright = 2*p + 2
        self.mark[chdleft] = self.mark.get(chdleft, 0) + chgval
        self.d[chdleft] += chgval * (mid-left)
        self.mark[chdright] = self.mark.get(chdright, 0) + chgval
        self.d[chdright] += chgval * (right-mid)
        return

nums = [10,11,12,13,14]
nums = [1,2,3,4,5, 6]

from pprint import pprint
# st = segmentTree(nums)
st = lazySegmentTree(nums)
pprint(st.d)
# print(len(st.d))
st.change(1,4,-3,0, len(nums), 0)
# after change : [1,-1,0,1,5,6]
print(st.getSum(1, 5, 0, len(nums), 0)) # 5

st.change(2,4,3,0, len(nums), 0)
# after change : [1, -1,3,4,5,6]
print(st.getSum(3,6, 0, len(nums), 0))  # 15