def findTarget(numList, target):
    if len(numList) == 0:
        return []

    if len(numList) == 1:
        if abs(numList[0]) == abs(target):
            if numList[0] == target:
                return ['1']
            else:
                return ['0']
        else:
            return []

    num0 = numList[0]
    left = findTarget(numList[1: ], target + num0)
    leftPart = ['0'+x for x in left if len(x) != 0]

    right = findTarget(numList[1: ], target - num0)
    rightPart = ['1'+x for x in right if len(x) != 0]

    return leftPart + rightPart

def findSumY(nums, visited,y):
    if y == 0:
        return True

    for i,num in enumerate(nums):
        if visited[i] == False:
            visited[i] = True
            if findSumY(nums, visited, y-num):
                return True
            visited[i] = False

    return False

def is5(nums):
    res = ['1' if x %5==0 else '0' for x in nums ]
    return ''.join(res)

def is3(nums):
    res = ['1' if x%3==0 else '0' for x in nums ]
    return ''.join(res)

def in5(b1, b5):
    for i,j in zip(b1, b5):
        if j=='1' and i != '1':
            return False
    return True
def in3(b1, b3):
    for i,j in zip(b1, b3):
        if j=='1' and i!='1':
            return False
    return True

while True:
    try:
        n, nums = int(input()), list(map(int, input().split()))

        # result = ['0' + x for x in findTarget(nums[1: ], nums[0]) if len(x)!=0]
        # print(result)

        # def has5not3(nums):
        #     r3 = [x for x in nums if x%3==0]
        #     r5 = [x for x in nums if x%5==0]
        #     return len(r5) > 0 and len(r3) == 0
    
        # def has3not5(nums):
        #     r3 = [x for x in nums if x%3==0]
        #     r5 = [x for x in nums if x%5==0]            
        #     return len(r3) >0 and len(r5) == 0

        b3 = is3(nums)
        b5 = is5(nums)
        others = []
        num3 ,num5 = [], []
        for i, (thr, fiv) in enumerate(zip(b3, b5)):
            if thr == '0' and fiv == '0':
                others.append(nums[i])
            if thr == '1':
                num3.append(nums[i])
            if fiv == '1':
                num5.append(nums[i])
        
        target = sum(num5) - sum(num3)
        y = (sum(num5) - sum(num3) + sum(others)) / 2
        if int(y) != y:
            print('false')
        else:    
            # result = [x for x in findTarget(others, target) if len(x)!=0]
            # print(len(result))
            # if len(result) > 0:
            if findSumY(others, [False]*len(others), y):
                print('true')
            else:
                print('false')


        # flag = 'false'
        # for res in result:
        #     a,b = [],[]
        #     for i,e in enumerate(res):
        #         if e == '0':
        #             a.append(nums[i])
        #         else:
        #             b.append(nums[i])
        #     # if (has5not3(a) and has3not5(b)) or (has5not3(b) and has3not5(a)):
        #     if in3(res, b3) ^ in5(res, b5):
        #         flag = 'true'
        #         break
        # print(flag)
        

    except Exception as e:
        # print('Break by Except Error : ' , e)
        break