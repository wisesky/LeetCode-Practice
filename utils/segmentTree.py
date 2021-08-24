
class segmentTree:
    """
    
    """
    def __init__(self, nums) -> None:
        length = len(nums)
        self.d = [0] * (2*length)
        self.a = nums
        self.build(0,length-1, 1)

    def build(self, s, t, p):
        """
        对[s,t]区间建立线段树，且当前编号为p
        """
        if  s == t:
            self.d[p] = self.a[s]
            return
        
        mid = s + (t-s)//2
        self.build(s, mid,p*2)
        self.build(mid+1, t, p*2+1)
        
        self.d[p] = self.d[2*p] + self.d[2*p+1]

    def update(self):
        pass

    def getSum(self):
        pass

nums = [10,11,12,13,14]
nums = [1,2,3,4,5,6]

st = segmentTree(nums)
print(st.d)