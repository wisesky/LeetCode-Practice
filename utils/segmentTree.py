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
        self.n = n
        self.d = [0] * (2*n-1)
        for i in range(length):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        i: 0-based
        p: 1-based
        相当于数组 nums[i] = val
        那么就需要修改二叉树关联所有值，类似于 堆中的 swim
        """
        p = i + self.n - 1
        self.d[p] = val
        while p > 0:
            p = (p-1) // 2
            self.d[p] = self.d[2*p+1] + self.d[2*p+2]
     
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
        注意， 这里d的数据类型dict是更优选择， 因为对nums 进行递归的二分法分割区间，
        会导致 二叉树并非是完全二叉树，会出现大量不连续的叶子结点，然而不连续的叶子结点仍然会占用索引空间
        如果用list，这个索引必须有值
        如果用dict， 则会节省很多索引空间
        eg:
                 21
             6       15
            3  3    9   6
           1 2 (3) 4 5  (6)
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


nums = [10,11,12,13,14]
nums = [1,2,3,4,5, 6]

st = segmentTree(nums)
print(st.d)
# print(len(st.d))
print(st.change(1,4,-3,0, len(nums), 0))
# after change : [1,-1,0,1,5,6]
print(st.getSum(1, 4, 0, len(nums), 0))