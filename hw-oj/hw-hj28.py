# from collections import defaultdict
# memo = defaultdict(bool)
import math
memo = {}

def isSS(n):
    if n in memo:
        return memo[n]

    square_n = math.floor(n**0.5)
    for i in range(2,square_n+1):
        if n % i == 0:
            memo[n] = False
            return False

    memo[n] = True
    return True

def isPairs(n1, n2):
    return isSS(n1+n2)

# 递归DFS 逻辑应该没问题 但是 TLE 无法验证
# optim: 其实 flag_chosen 可以用列表的方式传递，
# 每次递归调用前修改值，调用完之后再恢复成原来的值
def searchPairs(nums, flag_chosen,length_res=0):
    if length_res < 2:
        return []
        
    length = len(nums)
    r_max = []
    for i, (n1, flag1) in enumerate(zip(nums, flag_chosen)):
        if flag1 == '1':
            continue
        for j in range(i+1, length):
            flag2 = flag_chosen[j]
            if flag2 == '1':
                continue
            n2 = nums[j]
            if isPairs(n1, n2):
                r1 = [(n1, n2)]
                new_flag_chosen = flag_chosen[ :i] + '1' + flag_chosen[i+1:j] + '1' + flag_chosen[j+1: ]
                # new_flag_chosen = '1'.join[flag_chosen[ :i] ,flag_chosen[i+1:j], flag_chosen[j+1: ]]
                # list_other = list_res[:i] + list_res[i+1:j] + list_res[j+1: ]
                r2 = searchPairs(nums, new_flag_chosen, length_res-2)
                r = r1 + r2
                if len(r) > len(r_max):
                    r_max = r
    
    return r_max

# 匈牙利算法
# 奇数 偶数 二分图 最大匹配
def find(odd_choose, used, matched, evens):
    # odd_choose : 为选中的单个 odd 挑选匹配的 even
    # used: len(evens) 此轮find 递归中，是否曾经为evens 调整过归属问题, 每一轮新的递归时候（切换新的odd_choose),used 被重置
    # matched :len(evens), 全局的匹配归属结果, id_even -> id_odd
    # evens: 偶数列表
    for i, even in enumerate(evens):
        if isPairs(odd_choose, even) and used[i] == 0:
            used[i] = 1
            if matched[i] == 0 or find(matched[i], used, matched, evens) :
                # 如果全局matched显示次even仍然处于未匹配状态
                # 或 虽然次even已经匹配过
                # 但是 此时占用的 这个even 的odd 还可以重新被分配 : find(even->odd, used, matched, evens) == True
                matched[i] = odd_choose
                return True
        
    return False      

while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))

        # DFS
        # flag_chosen = '0'*len(nums)
        # list_result = searchPairs(nums, flag_chosen, len(nums))
        # print(len(list_result))

        # 二分图解法
        odds = []
        evens = []
        for num in  nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        result = 0
        matched = [0] * len(evens)
        for odd in odds:
            used = [0] * len(evens)
            flag = find(odd, used, matched, evens)
            if flag:
                result += 1
        
        print(result)

    except:
        break