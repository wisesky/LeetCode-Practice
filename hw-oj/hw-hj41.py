from functools import reduce
while True:
    try:
        n = int(input())
        weights = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        
        res = set()
        res.add(0)

        for i in range(n):
            weight = weights[i]
            num = nums[i]

            wets = [weight*j for j in range(1, num+1)]
            upds = []
            for r in res:
                upds += [r+x for x in wets]
            res.update(upds)

        result = len(res)
        print(result)
        print(res)
    except:
        break