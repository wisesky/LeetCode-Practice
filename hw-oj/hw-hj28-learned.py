# 二分图最大匹配
# 匈牙利算法

def issu(x):
    tem = 2
    while tem**2<=x:
        if x%tem==0:
            return False
        tem+=1
    return True
def find(a,used,match,even):
    for i in range(0,len(even)):
        if issu(a+even[i]) and used[i]==0:
            used[i]=1
            if match[i]==0 or find(match[i],used,match,even):
                match[i] = a
                return True
    return False

try:
    while True:
        n = input()
        n = int(n)
        l = list(map(int,input().split()))
        odd,even = [],[]
        for i in range(n):
            if l[i]%2==0:
                even.append(l[i])
            else:
                odd.append(l[i])
        result = 0
        match = [0]*len(even)
        for i in range(0,len(odd)):
            used = [0]*len(even)
            if find(odd[i],used,match,even):
                result+=1
        print(result)
except:
    pass
